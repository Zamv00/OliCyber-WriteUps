const encoded = 'aXQwNG5kXzExbHM0X3ZuXzMzdmQzMXJzX190dGhuMzNfMXNsMGNse3VDdEUxUzBBblQhSX0=';

const data = atob(encoded);
let result = new Array(data.length);

for (let i = 0, j = data.length - 1, k = false; j - i >= 0; k = k ? (i++, false) : (j--, true)) {

    const pos = k ? i : j;
    result[pos] = data[j - i];
}

console.log(result.join(""));
 
//ITASEC{cl13nt_s1d3_v4l1d4ti0n_1s_n3v3r_th3_s0lut10n!}