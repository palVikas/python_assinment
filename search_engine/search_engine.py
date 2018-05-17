import webbrowser

get_content  = open("source_code.txt", "r+")
get_text = get_content.read()


def get_link(page):
     start_link = page.find('<a href =')
     if(start_link ==(-1)):
         return None,0

     start_quote = page.find('"',start_link)
     end_quote = page.find('"',start_quote+1)
     url = page[start_quote+1:end_quote]
     return url , end_quote

def get_all_links(page):
    url_container =[]
    while True:
        url , end_quote = get_link(page)
        if url:
            url_container.append(url)
            page = page[end_quote:]
        else:
            break
    return url_container

def extract_links(linksList):
     for link in linksList:
          webbrowser.open(link)


all_link_list = get_all_links(get_text)
print(all_link_list)

extract_links(all_link_list)

get_content.close()

