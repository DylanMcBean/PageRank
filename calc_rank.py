import numpy as np
import json
import re
import os


os.system("clear")
print("Calculating Page Rank")
try:
    with open("output.json", encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_data = sorted(json_data, key=lambda x: x['url'])

    unique_links = set()
    site_links = []

    print("Getting Unique Links")
    for link in json_data:
        unique_links.add(link['url'])
        if link['url'] not in site_links:
            site_links.append(link['url'])
        for ilink in link['links']:
            unique_links.add(ilink)
except:
    print("Json Data Is Empty, this may be because the website is refusing scanning.")
    exit()

unique_links = sorted(list(unique_links))
print(f"Number of Unique Links found: {len(unique_links):,}")
print(f"Number of Website Pages: {len(site_links):,}")

adjacency_matrix = np.zeros((len(unique_links), len(unique_links)))

print("Creating Adjacency Matrix")
for link in json_data:
    for ilink in link['links']:
        adjacency_matrix[unique_links.index(
            link['url']), unique_links.index(ilink)] += 1


# change adjacency matrix to show probabilities
# we do this by dividing the links value by total links of that page
print("Converting Adjacency Matrix to probabilities")

# Create a dictionary to store the number of links for each page
link_counts = {link: max(len(json_data[site_links.index(
    link)]['links']), 1) for link in unique_links if link in site_links}

# Set the probability for pages with no outgoing links
default_prob = 1 / len(unique_links)

for i, link in enumerate(unique_links):
    links_count = link_counts.get(link, default_prob)
    for j in range(len(unique_links)):
        adjacency_matrix[i, j] /= links_count

# now we iterate over the array with a random vector
rand_vector = np.random.rand(len(unique_links))

# transpose adjacency matrix
print("Transposing Adjacency Matrix")
adjacency_matrix = adjacency_matrix.T

# Set the maximum number of iterations
max_iterations = 100000

# Set the convergence threshold
convergence_threshold = 1e-10

rand_vector_backup = adjacency_matrix.copy()

for iterations in range(1, max_iterations + 1):
    print(f"Matrix Mult Iteration: {iterations:,}\r", end="")
    # Multiply adjacency matrix by vector
    rand_vector = np.dot(adjacency_matrix, rand_vector)
    # Normalize vector
    rand_vector /= np.linalg.norm(rand_vector)

    # Check for convergence
    if np.linalg.norm(rand_vector - rand_vector_backup) <= convergence_threshold:
        # check if the ranking has changed , if so, dont change
        vector_rank = [x[0] for x in sorted(zip(range(len(rand_vector)), list(
            rand_vector)), key=lambda x: x[1], reverse=True)]
        backup_vector_rank = [x[0] for x in sorted(zip(
            range(len(rand_vector_backup)), list(rand_vector_backup)), key=lambda x: x[1], reverse=True)]
        if vector_rank == backup_vector_rank:
            break
    rand_vector_backup = rand_vector.copy()

# print pages in ranked order
page_rank = []
for link in json_data:
    index = unique_links.index(link['url'])
    page_rank.append([rand_vector[index], link['url']])

# Sort the page rank in descending order by rank score
page_rank.sort(key=lambda x: x[0], reverse=True)

# Write the page rank to a file
with open("page_rank.txt", "w") as f:
    max_width = max(len(x[1]) for x in page_rank)+2
    f.write(f" PAGE RANK |{'LINK':^{max_width}}| RANK SCORE\n")
    print(f"\nTop 25 Links\n PAGE RANK |{'LINK':^{max_width}}| RANK SCORE")
    for i, (rank_score, link) in enumerate(page_rank):
        f.write(f"{(i+1):^11}| {link:<{max_width-1}}| {rank_score}\n")
        if i < 25:
            print(f"{(i+1):^11}| {link:<{max_width-1}}| {rank_score}")

# Print the page rank to the console
print("\nPage rank written to page_rank.txt")
