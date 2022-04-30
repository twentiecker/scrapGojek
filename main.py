import scrolling
import writing

url = "https://www.gojek.com/id-id/products/"
file_name = "gojek_produk"

scroll = scrolling.Scrolling()
write = writing.Writing()

print("===== Start Scrolling =====")
scroll.scroll(url)
print("===== Finish Scrolling =====")

# Get category content
page_soup = scroll.page_soup
content_soup = page_soup.find_all("section", {"data-module": "pull-margin"})
print(len(content_soup))

# Scraping category by level
list_category = []
for x in content_soup:
    level1_tag = x.find("h2")
    print(level1_tag.text.strip())
    list_category.append(level1_tag.text.strip())
    level2_tag = x.find_all("img")
    for y in level2_tag:
        y1 = y["alt"].strip()
        if y1:
            print(f";{y1}")
            list_category.append(f";{y1}")
            cat_lv3 = y1.replace("Gojek", "").strip()

            print("===== Start Scrolling Lv3 =====")
            url_lv3 = f"https://www.gojek.com/{cat_lv3.lower()}"
            scroll.scroll(url_lv3)
            print("===== Finish Scrolling Lv3 =====")

            # Get category content lv3
            page_soup_lv3 = scroll.page_soup
            level3_tag = page_soup_lv3.find_all("h4",
                                                {"c-card__title c-card--base-1__title c-card__title--small"})
            for a in level3_tag:
                print(f";;{a.text.strip()}")
                list_category.append(f";;{a.text.strip()}")

print("===== Start Writing =====")
write.write(file_name, "Level 1;Level 2;Level 3\n", list_category)
print("===== Finish Writing =====")
