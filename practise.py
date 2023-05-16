import requests
from bs4 import BeautifulSoup
import json
# page = requests.get(
#     "https://www.factcheck.org/2023/04/scicheck-no-evidence-excess-deaths-linked-to-vaccines-contrary-to-claims-online/")
# soup = BeautifulSoup(page.content, 'html.parser')

html = '''
<p dir="ltr">
    <span>Another issue being monitored by scientists is whether boosting could hurt a person’s ability to respond to a future variant, as we have </span>
    <a href="https://www.factcheck.org/2022/02/scicheck-covid-19-booster-enhances-protection-contrary-to-immune-fatigue-claims/" target="_blank" rel="noopener noreferrer" data-auth="NotApplicable" data-safelink="true" data-linkindex="43">
        <span>written</span>
    </a>
    <span>. But Wherry, who has been following this topic, said there is no indication that is a current risk. “From the data that exists, I see no concern about that whatsoever,” he said. Some animal studies suggest that giving an omicron-only vaccine as a first vaccine dose in animals could be detrimental, he added, but that’s not what is being given to people.</span>
</p>
<h3 dir="ltr">
    <span>What do experts say about who should get the updated shots, and when?</span>
</h3>
<div>
    <p>
        <span>There is broad agreement that older people and those at higher risk of developing severe COVID-19 should get the new boosters. But experts differ on whether young, healthy people should get another dose.</span>
    </p>
    <p>
        <span>“I don't think that a healthy young person who has already received three doses frankly needs another dose, because I think they are protected against serious illness,” Offit said. “After about six months after their last dose, they're not going to be as protected against mild illness, but that's true of all infections like this one, meaning short incubation period, mucosal infections.”</span>
    </p>
    <p>
        <span>Offit still recommends that people over 75 years old, those with significant underlying health problems and those who are immunocompromised seek out the shots. Those are the groups, he said, that have benefited from the previous boosters.</span>
    </p>
</div>
'''

soup = BeautifulSoup(html, "html.parser")
span_tags = soup.find_all("span")

text_list = [span.get_text(strip=True) for span in span_tags]

print(text_list)



'''
base_url = "https://www.factcheck.org/scicheck/page/"
num_pages = 51  
href_list = []
for page_num in range(1, num_pages + 1):
    url = f"{base_url}{page_num}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    article_elements = soup.find_all("article")

    for article_element in article_elements:
        a_tag = article_element.find("a")
        if a_tag:
            href = a_tag["href"]
            href_list.append(href)

print(href_list)
with open("all_links.json", "w") as file:
    json.dump(href_list, file)

page = requests.get('https://www.factcheck.org/scicheck/')
soup = BeautifulSoup(page.content, 'html.parser')

article_elements = soup.find_all("article")

href_list = []

for article_element in article_elements:
    a_tag = article_element.find("a")
    if a_tag:
        href = a_tag["href"]
        href_list.append(href)

print(href_list)

page_title = soup.title.text[:-15]
page_author = soup.find('p', class_='byline').text
page_posted = soup.find('p', class_='posted-on').text

sci_digest = soup.find("h2", string="SciCheck Digest")
heading_tag = soup.find("h2", string="Full Story")
next_heading_tag = heading_tag.find_next("h2", string="Sources")
issues_tag = soup.find_all("li", class_="issue")

sci_digest_list = []
p_tags = sci_digest.find_next_siblings("p")
for p in p_tags:
    sci_digest_list.append(p.text)
# for p_text in sci_digest_list:
#     print(p_text,"\n")

paragraph_list = []
for sibling in heading_tag.find_next_siblings():
    if sibling.name == "h2" and sibling == next_heading_tag:
        break
    elif sibling.name == "p":
        paragraph_list.append(sibling)
# for paragraph_tag in paragraph_list:
#     print(paragraph_tag.text)

sentences_with_citations=[]
citation_list = []
for paragraph_tag in paragraph_list:
    link_tags = paragraph_tag.find_all("a")
    for link_tag in link_tags:
        citation_list.append(link_tag["href"])
        if link_tag.has_attr("href") and link_tag["href"].startswith("http"):
            link_text = link_tag.get_text().strip()
            escaped_text = re.escape(link_text)
        for sentence in re.findall(f"[^.]*?{escaped_text}[^.]*\.", soup.get_text()):
            sentences_with_citations.append(sentence)

# for citations in citation_list:
#     print(citations)

print(len(sentences_with_citations))
print(len(citation_list))
issue_list = []
for issues in issues_tag:
    issue_list.append(issues.text[6:])
# for iss in issue_list:
#     print(iss)

image_div = soup.find("div", class_="wp-block-image")
image_caption = soup.find("figcaption", class_="wp-element-caption").text

img_tag = image_div.find("img")
img_src = img_tag['src']
print(img_src)
print(image_caption)

import requests
from bs4 import BeautifulSoup

# page = requests.get(
#     "https://www.factcheck.org/2023/04/scicheck-no-evidence-excess-deaths-linked-to-vaccines-contrary-to-claims-online/")
# soup = BeautifulSoup(page.content, 'html.parser')

page = requests.get('https://www.factcheck.org/2023/04/scicheck-fewer-cases-of-flu-due-to-pandemic-precautions-contrary-to-viral-claim/')
soup = BeautifulSoup(page.content, 'html.parser')

heading_tag = soup.find("h2", string="Full Story")
next_heading_tag = heading_tag.find_next("h2", string="Sources")
paragraph_tags = []
for sibling in heading_tag.find_next_siblings():
    if sibling.name == "h2" and sibling == next_heading_tag:
        break
    elif sibling.name == "p":
        paragraph_tags.append(sibling)
for paragraph_tag in paragraph_tags:
    print(paragraph_tag.text)

for paragraph_tag in paragraph_tags:
    link_tags = paragraph_tag.find_all("a")
    for link_tag in link_tags:
        print(link_tag["href"])

issue_tags = soup.find_all("li", class_="issue")
for issue_tag in issue_tags:
    print(issue_tag.text[6:])


import requests
from bs4 import BeautifulSoup
import json

page = requests.get(
    "https://www.factcheck.org/2023/04/scicheck-no-evidence-excess-deaths-linked-to-vaccines-contrary-to-claims-online/")
soup = BeautifulSoup(page.content, 'html.parser')
page_title = soup.title.text[:-15]
page_author = soup.find('p', class_='byline').text
page_posted = soup.find('p', class_='posted-on').text


page_subheading = soup.find('h2', class_='wp-block-heading')
# print(page_subheading.text)


# for headlines in soup.find_all("h2", class_='wp-block-heading'):
#     print(headlines.text)

# for i in soup.find('div', class_="'entry-content"):


# for i in soup.find_all(class_='wp-block-heading'):
#     j = i.find_all('p')
#     print(j)



# Print text
s = soup.find_all('div', class_='entry-content')
for i in s:
    if str(i).find('</h2>'):
        print(i)
        



# for i in lines

# print(s)
all_lines=[]
# for line in lines:
    # all_lines.append(line.text)
    # print(line.text)
# print(all_lines)

# Print entire text
# print(soup.get_text()) 

# Print all links
# for link in soup.find_all('a'):
    # print(link.get('href'))


# dictionary = {
# 	"title": page_title,
# 	"rollno": 56,
# 	"cgpa": 8.6,
# 	"phonenumber": "9976770500"
# }

# # Serializing json
# json_object = json.dumps(dictionary, indent=4)

# # Writing to sample.json
# with open("sample.json", "w") as outfile:
# 	outfile.write(json_object)

# heading_tag = soup.find("h2", class_="wp-block-heading")
# separator_tag = soup.find("hr", class_="wp-block-separator")
# next_tag = heading_tag.find_next_sibling()
# paragraph_tag = None
# while next_tag is not None:
#     if next_tag.name == "p" and next_tag.find(separator_tag.name, separator_tag.attrs) is not None:
#         paragraph_tag = next_tag
#         break
#     next_tag = next_tag.find_next_sibling()
# if paragraph_tag is not None:
#     print(paragraph_tag.text)
# else:
#     print("Paragraph tag not found.")


# Find the heading tag
# heading_tag = soup.find("h2", text="Full Story")
# next_tag = heading_tag.find_next_sibling()
# paragraph_tag = next_tag.find_next_sibling("p")
# print(paragraph_tag.text)

# heading_tag = soup.find("h2", text="Full Story")
# for p_tag in heading_tag.find_all_next("p"):
#     print(p_tag.text)

# heading_tags = soup.find_all("h2", text="Full Story")
# for heading_tag in heading_tags:
#     paragraph_tag = heading_tag.find_next_sibling("p")
#     print(paragraph_tag.text)

# heading_tag = soup.find("h2", text="Full Story")
# paragraph_tags = heading_tag.find_next_siblings("p", until=lambda tag: tag == "h2")
# for paragraph_tag in paragraph_tags:
#     print(paragraph_tag.text)

# h2_tags = soup.find_all("h2")
# for i in range(len(h2_tags)-1):
#     if h2_tags[i].text == "Full Story":
#         heading_tag = h2_tags[i]
#         next_heading_tag = h2_tags[i+1]
#         paragraph_tags = heading_tag.find_next_siblings("p", until=lambda tag: tag == next_heading_tag)
#         for paragraph_tag in paragraph_tags:
#             print(paragraph_tag.text)


# # Find the first h2 tag with the text "Full Story"
# heading_tag = soup.find("h2", string="Full Story")
# print(heading_tag)
# # Find the next h2 tag with the text "Sources"
# next_heading_tag = heading_tag.find_next("h2", string="Sources")
# print(next_heading_tag)
# # Find all the p tags between the two h2 tags
# paragraph_tags = heading_tag.find_next_siblings("p", until=lambda tag: tag == next_heading_tag)
# print(paragraph_tags)
# # Loop through all the paragraph tags and extract the text content
# for paragraph_tag in paragraph_tags:
#     print(paragraph_tag.text)
'''