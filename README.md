TUGAS 4:
//Apa kegunaan {% csrf_token %} pada elemen form? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?
Pada elemen form, {% csrf_token %} berfungsi untuk membuat dan meng-input token keamanan  CSRF (Cross-Site Request Forgery) ke dalam form HTML. Token keamanan CSRF tersebut bertujuan untuk mencegah serangan CSRF: jenis serangan web dalam bentuk manipulasi tindakan pengguna terautentikasi tanpa sepengetahuan atau persetujuannya.
Django akan menolak permintaan POST yang dikirimkan oleh pengguna apabila form tidak terdapat {% csrf_token %}. Alasannya, pada setiap permintaan POST yang diterima, eksistensi token CSRF akan diperiksa oleh Django, secara default. Django akan menganggap permintaan tersebut tidak valid dan menolak untuk memprosesnya, apabila token tidak ada atau tidak cocok.

//Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat form secara manual.
Kita dapat membuat elemen form secara manual. Caranya, kita perlu membuat sebuah class form di dalam file forms.py, mengatur field-field dan argumen-argumen untuk setiap field, mengimport form tersebut ke dalam view, dan menampilkan form di dalam template dengan tag-tag yang sesuai.

//Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
1. Pengguna mengisi HTML form yang telah disediakan oleh website, dan menekan tombol submit.
2. Browser mengirimkan data form tersebut ke server melalui HTTP POST request.
3. Server menerima request tersebut dan menjalankan view yang telah diatur untuk form tersebut.
4. View melakukan validasi data form untuk memastikan bahwa data yang dimasukkan pengguna sesuai dengan aturan yang telah ditentukan. Jika terdapat kesalahan, view akan menampilkan kembali form dengan pesan error yang sesuai.
5. Jika data form valid, view akan menyimpan data tersebut ke dalam database dengan menggunakan model yang telah diatur sebelumnya.
6. Setelah data berhasil disimpan ke dalam database, view akan meredirect pengguna ke halaman sukses atau menampilkan data yang telah disimpan pada halaman yang sesuai.
7. Pada halaman yang sesuai, view akan menampilkan data yang telah disimpan pada template HTML dengan menggunakan tag-tag yang sesuai seperti `{% for %}` atau `{{ }}`.

//Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuka study_tracker/views.py
2. Menambahkan import redirect, UserCreationForm, dan messages
3. Membuat fungsi bernama register yang menerima parameter request, yang berisi kode untuk menghasilkan formulir registrasi secara otomatis {{ UserCreationForm(request.POST) }} dan menghasilkan akun pengguna ketika data di-submit dari form {{ form.save() }}
4. Membuat file register.html pada folder study_tracker/templates untuk membuat halaman register
5. Membuat form dengan generator {{ form.as_table }}
6. Membuka study_tracker/urls.py
7. Mengimpor fungsi register dan menambahkan path-nya pada urls.py

8. Membuka study_tracker/views.py
9. Menambahkan import authenticate dan login
10. Membuat fungsi bernama login_user yang menerima parameter request, yang berisi kode untuk mengautentikasi pengguna yang ingin login
11. Membuat file login.html pada folder study_tracker/templates untuk membuat halaman login
12. Membuka study_tracker/urls.py
13. Mengimpor fungsi login_user dan menambahkan path-nya pada urls.py
14. Memoodifikasi variable name pada context dalam fungsi show_tracker yang berada pada study_tracker/views.py menjadi {{'name': request.user.username}} agar dapat menampilkan nama sesuai pengguna yang logged in.

15. Membuka study_tracker/views.py
16. Menambahkan import logout
17. Membuat fungsi bernama logout_user yang menerima parameter request, yang berisi kode untuk melakukan mekanisme logout
18. Membuka study_tracker/templates/assignment_list.html 
19. Menambahkan kode pada assignment_list.html untuk menambah tombol logout
20. Membuka study_tracker/urls.py
21. Mengimpor fungsi logout_user dan menambahkan path-nya pada urls.py

22. Membuka study_tracker/views.py
23. Menambahkan import login_required
24. Menambahkan kode {{ @login_required(login_url='/money_tracker/login/') }} di atas fungsi show_tracker agar halaman money tracker hanya dapat diakses oleh pengguna yang sudah login (terautentikasi).

25. Membuka study_tracker/views.py
26. Menambahkan import HttpResponseRedirect, reverse, dan datetime
27. Pada fungsi login_user, menambahkan fungsi untuk menambahkan cookie yang bernama last_login untuk melihat kapan terakhir kali pengguna melakukan login. 
28. Pada fungsi show_tracker, menambahkan potongan kode {{ 'last_login': request.COOKIES['last_login'] }} ke dalam variabel context, untuk menambahkan variabel yang nantinya memunculkan waktu terakhir login
29. Mengubah fungsi logout_user untuk menambahkan mekanisme penghapusan cookie last_login saat pengguna melakukan logout.
30. Membuka berkas tracker.html dan menambahkan potongan kode {{ Sesi terakhir login: {{ last_login }} }} di antara tabel dan line break tag untuk menampilkan data last login.


TUGAS 3:
//Apakah kita dapat menginput data selain melalui form? Namun mengapa form dapat dikatakan lebih baik daripada menggunakan cara tersebut?

Ya, kita dapat menginput data selain melalui form, seperti menggunakan django built-in shell atau django admin. Namun, menggunakan form dapat dikatakan lebih baik daripada cara lainnya karena form dapat digunakan untuk menentukan aturan validasi untuk setiap fields, memastikan bahwa data yang dimasukkan oleh pengguna valid sebelum disimpan ke database. Hal ini dapat membantu mencegah kesalahan dan meningkatkan kualitas data secara keseluruhan. Selain itu, form juga dapat dikustomisasi untuk memenuhi persyaratan tertentu dan dapat diperluas untuk menyertakan fungsionalitas tambahan seperti aturan validasi kustom, widget, dan input masks.

//Jelaskan perbedaan antara JSON, XML, dan HTML!

- JSON adalah format pertukaran data yang ringan dan sepenuhnya language-independent. JSON berbasis 
JavaScipt dan mudah dimengerti dan di-generate. Format JSON mirip dengan maps pada Java.

- XML merupakan mark-up language yang dirancang untuk membawa data. XML mendefinisikan seperangkat aturan untuk mengkodekan dokumen dalam format yang dapat dibaca oleh manusia dan mesin. Perbedaan yang cukup terlihat antara XML dan JSON adalah XML merupakan mark-up language yang menggunakan struktur tag untuk merepresentasikan data

- HTML merupakan markup language yang digunakan untuk menampilkan data, bukan membawa data seperti JSON dan XML.

source: https://www.geeksforgeeks.org/difference-between-json-and-xml/, https://www.geeksforgeeks.org/html-vs-xml/ 

//Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform.

Pengiriman data adalah aspek penting dari implementasi platform karena beberapa alasan:
1. Data delivery memastikan bahwa data tersedia saat dibutuhkan, dan pengguna dapat mengaksesnya dengan mudah dan efisien, terlepas dari lokasi atau perangkat yang mereka gunakan.
2. Data delivery membantu memastikan bahwa data diproses dan dikirimkan secara real-time untuk mendukung operasi bisnis yang penting.
3. Data delivery dapat mengoptimalkan pemanfaatan sumber daya dengan memastikan bahwa data dikirimkan hanya pada saat dibutuhkan, sehingga menghasilkan kinerja yang lebih baik dan penghematan biaya.
4. Data delivery dapat meningkatkan keamanan data dengan menyediakan protokol transfer dan penyimpanan data yang aman
5. Data delivery dapat memastikan bahwa platform dapat menangani lalu lintas data yang semakin meningkat tanpa mengorbankan kinerja atau pengalaman pengguna.

//Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Menjalankan virtual environment
2. Membuat file baru pada folder study_tracker dengan nama forms.py untuk membuat struktur form yang dapat menerima data transaksi baru.
3. Membuka file views.py yang ada pada folder study_tracker dan menambahkan import HttpResponseRedirect, TransactionRecordForm, dan reverse.
4. Membuat fungsi baru dengan nama create_assignment pada file views.py yang menerima parameter request, yang digunakan untuk menghasilkan formulir yang dapat menambahkan data transaksi secara otomatis ketika data di-submit dari form.
5. Membuat berkas HTML baru dengan nama create_assignment.html pada folder study_tracker/templates.
6. Membuka urls.py yang ada pada folder study_tracker dan import fungsi create_assignment, lalu menambahkan path url ke dalam urlpatterns untuk mengakses fungsi create_assignment
7. Membuka tracker.html lalu menambahkan button tambah transaksi baru

8. Membuka views.py yang ada pada folder study_tracker dan membuat fungsi show_xml dan show_json yang menerima parameter request
9. Menambahkan import HttpResponse dan Serializer pada bagian views.py paling atas.
10. Membuat sebuah variabel di dalam fungsi show_xml dan show_json yang menyimpan hasil query dari seluruh data yang ada pada Assignment.
11. Menambahkan return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML dan JSON dan parameter content_type="application/xml" (untuk format xml) dan parameter content_type="application/json" (untuk format json)
12. Membuka urls.py yang ada pada folder study_tracker dan import fungsi show_xml & show_json.
13. Menambahka path url ke dalam urlpatterns untuk mengakses kedua fungsi yang sudah diimpor sebelumnya.

14. Membuka views.py yang ada pada folder money_tracker dan membuat sebuah fungsi show_xml_by_id dan show_json_by_id yang menerima parameter request dan ID.
15. Membuat sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari data dengan ID tertentu yang ada pada Assignment.
16. Menambahkan return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON atau XML dan parameter content_type dengan value "application/xml" (untuk format XML) atau "application/json" (untuk format JSON).
17. Membuka urls.py yang ada pada folder study_tracker dan impor fungsi show_xml_by_id dan show_json_by_id.
18. Menambahkan path url ke dalam urlpatterns untuk mengakses dua fungsi yang sudah diimpor sebelumnya.


TUGAS 2:
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