//Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya 
dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html

Alur request client ke web aplikasi berbasis django:
1. Django menerima URL, memeriksa berkas urls.py, dan memanggil tampilan (views) 
    yang sesuai dengan URL.
2. Tampilan, yang terletak di views.py, memeriksa models yang relevan.
3. Models diimpor dari file models.py.
4. Views kemudian mengirimkan data ke template yang telah ditentukan di dalam folder template.
5. Templat berisi tag HTML dan Django, dan dengan data itu mengembalikan konten HTML 
    yang telah selesai kembali ke browser.

source: w3schools.com

//Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web 
berbasis Django tanpa menggunakan virtual environment?

    Virtual Environment memungkinkan kita untuk memiliki lingkungan yang stabil, reproducible, 
dan portabel. Kita dapat mengendalikan versi paket mana yang diinstal dan kapan paket tersebut 
di-upgrade. Kita juga dapat memiliki venv sebanyak yang kita inginkan. Dengan kata lain, 
virtual environment membantu kita untuk mengisolasi proyek, sehingga perubahan terhadap 
versi paket instalasi dapat diatur dan tidak mempengaruhi proyek lainnya.

    Sebenarnya, kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan 
virtual environment. Namun, jika kita mengunduh versi paket instalasi terbaru, 
setiap update akan terinstalasi secara default ke global environment, yang akan mempengaruhi 
seluruh proyek. Ini tentunya menjadi masalah karena tiap proyek belum tentu membutuhkan 
versi paket instalasi yang terbaru.

source: https://csguide.cs.princeton.edu/software/virtualenv#:~:text=Virtual%20environments%20let%20you%20have,many%20venvs%20as%20you%20want.
, https://realpython.com/python-virtual-environments-a-primer/#why-do-you-need-virtual-environments 

//Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

1. Menggunakan perintah "git clone" untuk menyalin repositorinya ke suatu lokasi 
    di dalam sistem berkas (filesystem) komputer.
2. Masuk ke dalam repositori yang sudah di-clone.
3. Menyalakan virtual environment.
4. Menginstal dependencies yang dibutuhkan untuk menjalankan aplikasi.
5. Membuat sebuah django-app bernama study_tracker dengan menggunakan perintah "manage.py 
    startapp study_tracker".
6. Melakukan routing pada django_project: membuka settings.py, lalu menambahkan aplikasi 
study_traker ke dalam variabel INSTALLED_APPS, agar dapat menjalankan aplikasi study_tracker.
7. Membuat model (models.py) pada aplikasi study_tracker yang bernama Assignment 
yang memiliki atribut:
    - name untuk nama tugas dengan tipe CharField,
    - subject untuk mata kuliah tugas dengan tipe CharField,
    - date untuk tenggat waktu tugas dengan tipe DateTimeField,
    - progress untuk indikator progress tugas dengan tipe IntegerField, dan
    - description untuk deskripsi tugas dengan tipe TextField.
8. Melakukan perintah "manage.py makemigrations" untuk mempersiapkan migrasi skema model 
    ke dalam database Django lokal.
9. Menjalankan perintah "manage.py migrate" untuk menerapkan skema model 
    yang telah dibuat ke dalam database Django lokal.
10. Membuat folder templates pada root folder dan membuat sebuah file baru bernama base.html. 
[file base.html telah terdeteksi sebagai file tempat pada django_project/settings.py]
11. Membuka views.py yang ada pada folder study_tracker dan membuat sebuah fungsi 
    yang menerima parameter request dan mengembalikan render(request, "tracker.html").
12. Membuat sebuah folder bernama templates di dalam folder aplikasi study_tracker dan 
    membuat sebuah berkas bernama tracker.html