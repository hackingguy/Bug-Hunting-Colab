[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/hackingguy/Bug-Hunting-Colab">
    <img src="https://d3eys52k95jjdh.cloudfront.net/wp-content/uploads/2019/06/google-dark.jpg" alt="Logo" height="200">
  </a>

  <h3 align="center">Bug Hunting Colab</h3>

  <p align="center">
    Use Google Tools Wisely
    <br />
  </p>
</p>

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hackingguy/Bug-Hunting-Colab/)


<!-- ABOUT THE PROJECT -->
## About The Project

[![Bug Hunting Colab][product-screenshot]](https://github.com/hackingguy/Bug-Hunting-Colab)

Used Google Tools in a wiser way! I made a Jupyter Notebook for google collab that is gonna provide you a VPS(Virtual Private Server) with 24 GB RAM, 60 GB Storage in just 5 min deploy and get a Linux Instance. 


<!-- GETTING STARTED -->
## Getting Started

To get it running simply follow below steps:

### Prerequisites

Don't worry, you only have to do this once per client machine.

  1. Download [Cloudflared (Argo Tunnel)](https://developers.cloudflare.com/argo-tunnel/downloads), then copy the absolute path to the cloudflare binary
  2. Now, you have to append the following to your SSH config file (usually under ~/.ssh/config in Linux and in C:/Users/\<Username\>/.ssh/config in Windows):
  ```
    Host *.trycloudflare.com
	  HostName %h
	  User root
	  Port 22
	  ProxyCommand <PUT_THE_ABSOLUTE_CLOUDFLARE_PATH_HERE> access ssh --hostname %h
  ```
2 ways of using it (**Argotunnel And Chrome Desktop**) are described in this [video](https://youtu.be/bJUr0SnBpEM).


<!-- USAGE EXAMPLES -->
## Usage

Just Click On `Open In Colab Button` And Run The Bug Hunting Colab Cell.<br><br>
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hackingguy/Bug-Hunting-Colab/)

<!-- CONTRIBUTING -->
## Shout Out

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Shout out to all the guys that helped to make this awesome

1. [Anugrahsr](https://github.com/Anugrahsr)
2. [aksl337](https://github.com/aksl337)



<!-- LICENSE -->
## License

Distributed under the GPL 3.0 License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Akash Chhabra - [@hackingguyak](https://twitter.com/hackingguyak) - akashchhabra710@gmail.com

Project Link: [https://github.com/hackingguy/Bug-Hunting-Colab](https://github.com/hackingguy/Bug-Hunting-Colab)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [ReconFTW](https://github.com/six2dez/reconftw)
* [Shell-Bot](https://github.com/botgram/shell-bot)
* [Google-Colab](https://colab.research.google.com)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/hackingguy/Bug-Hunting-Colab.svg?style=for-the-badge
[contributors-url]: https://github.com/hackingguy/Bug-Hunting-Colab/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/hackingguy/Bug-Hunting-Colab.svg?style=for-the-badge
[stars-url]: https://github.com/hackingguy/Bug-Hunting-Colab/stargazers
[forks-shield]: https://img.shields.io/github/forks/hackingguy/Bug-Hunting-Colab.svg?style=for-the-badge
[forks-url]: https://github.com/hackingguy/Bug-Hunting-Colab/network/members
[issues-shield]: https://img.shields.io/github/issues/hackingguy/Bug-Hunting-Colab.svg?style=for-the-badge
[issues-url]: https://github.com/hackingguy/Bug-Hunting-Colab/issues
[license-shield]: https://img.shields.io/github/license/hackingguy/Bug-Hunting-Colab.svg?style=for-the-badge
[license-url]: https://github.com/hackingguy/Bug-Hunting-Colab/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/hackingguy
[product-screenshot]: https://i.imgur.com/zHXqeY3.png
