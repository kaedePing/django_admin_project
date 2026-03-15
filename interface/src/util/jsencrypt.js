import JSEncrypt from 'jsencrypt';

// 密钥对生成 http://web.chacuo.net/netrsakeypair

const publicKey = "-----BEGIN PUBLIC KEY-----\n" +
    "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAr9OYQUkJI1cW51b0OmIV\n" +
    "D+pzU9lzpNtnclN3LN8xvYr5Y2Mx0HcuEq4XYOkZJq0npaPf2DSww6Jb+X3qM1WH\n" +
    "brJoqjoC/I5cfqZNVeDqrODjF2NVAKOtalLRr/TU7QvYEhDu9l62C3OTH2zoT1RR\n" +
    "jG1PJm4xCq2OYOy0NVxzrv26Vxnou8Lsco80FyO9teyiu1OrKcOzTmKi21DVXzVl\n" +
    "hsbyeS2ayRfxVLJSteR//glRvgiAiUcsG4iky1Z4eXxaGeaWdrIYFff/o8jErIYN\n" +
    "1ZTvHujWJO3SW4sid8ObUhHFBh3Sk2QtDR0xvlPrBsbK0ttd5eUztqXTSJ8HIKFF\n" +
    "OwIDAQAB\n" +
    "-----END PUBLIC KEY-----\n"

const privateKey = "-----BEGIN RSA PRIVATE KEY-----\n" +
    "MIIEowIBAAKCAQEAr9OYQUkJI1cW51b0OmIVD+pzU9lzpNtnclN3LN8xvYr5Y2Mx\n" +
    "0HcuEq4XYOkZJq0npaPf2DSww6Jb+X3qM1WHbrJoqjoC/I5cfqZNVeDqrODjF2NV\n" +
    "AKOtalLRr/TU7QvYEhDu9l62C3OTH2zoT1RRjG1PJm4xCq2OYOy0NVxzrv26Vxno\n" +
    "u8Lsco80FyO9teyiu1OrKcOzTmKi21DVXzVlhsbyeS2ayRfxVLJSteR//glRvgiA\n" +
    "iUcsG4iky1Z4eXxaGeaWdrIYFff/o8jErIYN1ZTvHujWJO3SW4sid8ObUhHFBh3S\n" +
    "k2QtDR0xvlPrBsbK0ttd5eUztqXTSJ8HIKFFOwIDAQABAoIBABygoH0ctaKt5tpC\n" +
    "w6AP4SsGusFPue8BFB4+rbw+GNyqGIHQoEc3aGZ9Nuw996ze64IiJOuQZKltsXj1\n" +
    "QeEaz2K8JKN2r47MZQ3v6M6PQNZmBUOFFk102OLjWiXCgLqZv5PtcuLlN9G0fyNS\n" +
    "OZ7U9TQehhEVRuHcsT5hu9OmWmWGv+wxIvqPorXxi4x7ItjT+O6iY9iNszdptUrg\n" +
    "RyINyfh8b1+9E4s4g8RPUbXXq38E5HyanSJa/Wv6iClG6UuIzPPWFVOKwZMnNaiw\n" +
    "8xkyJs6Bf7NUMhwFMo4ZtLj985dV5r2ShhP35IlZx/zgedz4g1ZyofPtX8Hc/hmF\n" +
    "AjfFCukCgYEA51SuPh93RypxFuK38ms2qRdC494cmQ65GZSNxP1B/H5QHdm8hLiV\n" +
    "GtUWdTVuf1n28NQpOj3hKLco2bYDmpsb9vt10Nr7LydpT5Q2k6Lf2LZnCC/V7bS+\n" +
    "tbp3jSaGtUMVtHJa8IaPA9UiSgjBfzDck2EOudR36CoCBmrWrf3ZiYkCgYEAwpOm\n" +
    "pSjk64bNDCJgB8yIU0g4BFGmRLLe41ytKN6vEfxZzem+hgmBEycjedyaSxf2/gVs\n" +
    "gZDi9CV1OeqCZFFRIQT199fb4LeM4YJqSXUZww0O+OVDjU1B2OgJZzaROfMSIo8y\n" +
    "UcERjyb2bC+Uuwte5CjOayvMMEcI7MAmkZGjW6MCgYBlEWlDOQoq7I8WOZ22a0Mp\n" +
    "Y0FVPyBterJCS9YYv7GJuEIWmJ+1uNNkMr8qHFsXht3N4FPW31w1JrjRTaWLccMp\n" +
    "CDo0MshVlLl9DDtAC4QTMbYYLJYh0bsUuNAsui1WmmWsPd4fghqPyRm/EM5BXL6y\n" +
    "IVCGvh5ZL6lM1nbO876MSQKBgGswOaJMZ+eTyAuCOFKzivoOE8XVUPoRa5XmrQGR\n" +
    "wvHuiW5U8P8X50Is0m9EZr8tgYQoasDplw0WQYDZPmGTJlVBTVruUBN4KiTk2jaD\n" +
    "SuDXpcLZUaBaygZ6tQtl1RUOYZQmPHsrF8g7l467m3x65BhennANnZuO1kzOAbE5\n" +
    "gLtvAoGBAITnIERqxYaib1RpTOjmt81b+v8osQVp8QiRVtO4R1K9hF0AawsNdhq4\n" +
    "1zk5AMhV3aN0jVep31sd84N9UutuUyWu4HUElItHYmhDF83JzB+pdCDlOMOeKpK1\n" +
    "ZGpT/oCDEkHJfuR7qJUUMLpLauMEAwUM+ex+179yGmD96UKt9UyS\n" +
    "-----END RSA PRIVATE KEY-----\n"

// 加密
export function encrypt(txt) {
  const encryptor = new JSEncrypt()
  encryptor.setPublicKey(publicKey) // 设置公钥
  return encryptor.encrypt(txt) // 对数据进行加密
}

// 解密
export function decrypt(txt) {
  const encryptor = new JSEncrypt()
  encryptor.setPrivateKey(privateKey) // 设置私钥
  return encryptor.decrypt(txt) // 对数据进行解密
}