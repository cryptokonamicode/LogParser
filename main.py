import re


def main():
    file_list = []
    ip_dict = {}
    ip_pattern = '\d+[.]\d+[.]\d+[.]\d+'
    time_pattern = '[[]\d+[\/]\w+[\/]\d+[:]\d+[:]\d+[:]\d+[ ][+]\d+[]]'
    get_pattern = '(?:"GET \/).+(?:HTTP\/1.1")'
    two_hundred_pattern = '(?:200) \d+ '
    # For URL and access, add more patterns and if statements as needed.
    # Got all in the original sample, not all in apache_log.
    url_pattern = '(?:http).+["]'
    url_pattern2 = '(?:"-")'
    access_pattern = '(?:Mozilla\/5.0) .+["]'
    access_pattern2 = '(?:Tiny Tiny) .+["]'
    # with open('Log_File.txt') as f: #test file
    with open('apache_log') as f: #longer test file
        lines = f.readlines()
    for line in lines:
        ip = re.findall(ip_pattern, line)
        time = re.findall(time_pattern, line)
        get = re.findall(get_pattern, line)
        two_hundred = re.findall(two_hundred_pattern, line)
        if re.match(url_pattern, line):
            url = re.findall(url_pattern, line)
        elif re.match(url_pattern2, line): #If it's not http, check for "-". Add more if statements as needed.
            url = re.findall(url_pattern2, line)
        else:
            url = re.findall(url_pattern, line) #just a blank value since we couldn't find the real one
        if re.match(access_pattern, line):
            access = re.findall(access_pattern, line)
        elif re.match(access_pattern2, line): #if it's not Mozilla, check for Tiny Tiny. Add more if statements as needed.
            access = re.findall(access_pattern2, line)
        else:
            access = re.findall(access_pattern, line) #just a blank value since we couldn't find the real one
        file_list.append(File(ip, time, get, two_hundred, url, access))
    for file in file_list:
        key = tuple(file.ip)
        ip_dict[key] = ip_dict.get(key, 0) + 1
        file.print()
    print("There are ", len(ip_dict.keys()), "unique IP addresses.")
    print(ip_dict)


class File:
    def __init__(self, ip, time, get, two_hundred, url, access):
        self.ip = ip
        self.time = time
        self.get = get
        self.two_hundred = two_hundred
        self.url = url
        self.access = access

    def print(self):
        print('IP address is: ', self.ip, 'Time is: ', self.time, 'GET is: ', self.get,
              '200 number is: ', self.two_hundred, 'URL is: ', self.url,
              'Access is: ', self.access)


if __name__ == '__main__':
    main()
