def get_link(page):
     start_link = page.find('<a href =')
     if(start_link ==(-1)):
         return None,0

     start_quote = page.find('"',start_link)
     end_quote = page.find('"',start_quote+1)
     url = page[start_quote+1:end_quote]
     return url , end_quote

def print_all_links(page):
    while True:
        url , end_quote = get_link(page)
        if url:
            print (url)
            page = page[end_quote:]
        else:
            break


print_all_links('............<a href = "www.facebook.com">.......<a href = "www.lolbook.com">..............<a href = "www.pagal.com">...................<a href = "www.instagrame.com">')
        
