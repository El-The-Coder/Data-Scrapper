import requests
import pandas as pd
from bs4 import BeautifulSoup

th = "https://www.jobs.id/lowongan-kerja?kata-kunci=part time"
halaman = requests.get(th)
hasil = BeautifulSoup(halaman.content, 'html.parser')
lowkers = hasil.find_all(class_="single-job-ads")

posisi = []
instansi = []
gaji = []

for p in lowkers:
  t1 = p.select("h3")
  t2 = t1[0].select("a")
  posisi.append(t2[0].get_text())

  t1 = p.select("p")
  t2 = t1[0].select("a")
  try:
    instansi.append(t2[0].get_text())
  except:
    instansi.append("-")
  t2 = t1[1].select("span")
  try:
    gaji.append(t2[1].get_text())
  except:
    gaji.append(t2[0].get_text())

lowker = pd.DataFrame({
  "Posisi": posisi,
  "Instansi": instansi,
  "Gaji":gaji
})
lowker
