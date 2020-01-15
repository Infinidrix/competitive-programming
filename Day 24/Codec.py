# https://leetcode.com/problems/encode-and-decode-tinyurl/

class Codec:
    
    def __init__(self):
        self.stored = {}
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = hash(longUrl)
        self.stored[key] = longUrl
        return "http://tinyurl.com/" + str(key)
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key = int(shortUrl.split("/")[-1])
        return self.stored[key]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
