# HF_D_PHYSICIAN

> A dimension table that contains the physicians' information.

**Description:** HF_D_PHYSICIAN  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MEDICAL_SPECIALTY` | VARCHAR(40) |  |  | The medical specialty of a physician. A NULL means the physician id field was blank and therefore no medical specialty was provided. |
| 2 | `NPI` | VARCHAR(200) |  |  | The Physician's NPI (National Provider Identifier). |
| 3 | `PHYSICIAN_ADDRESS` | VARCHAR(255) |  |  | The full address of the physician. |
| 4 | `PHYSICIAN_ADDRESS_2` | VARCHAR(255) |  |  | The second line of the address for the ordering physician. |
| 5 | `PHYSICIAN_CALL_INSTRUCTIONS` | VARCHAR(300) |  |  | Text field to be used to indicate any specific protocol or instructions to be followed when calling the physician number. |
| 6 | `PHYSICIAN_CITY` | VARCHAR(100) |  |  | The city of the physician. |
| 7 | `PHYSICIAN_COUNTRY` | VARCHAR(100) |  |  | The country of the physician. |
| 8 | `PHYSICIAN_COUNTY` | VARCHAR(100) |  |  | The county of the physician. |
| 9 | `PHYSICIAN_EMAIL` | VARCHAR(100) |  |  | The physician email address. |
| 10 | `PHYSICIAN_EXTENSION` | VARCHAR(100) |  |  | The physician's phone extension. |
| 11 | `PHYSICIAN_FAX` | VARCHAR(50) |  |  | The primary phone number of the physician. |
| 12 | `PHYSICIAN_FIRST_NAME` | VARCHAR(100) |  |  | The first name of the physician. |
| 13 | `PHYSICIAN_ID` | DOUBLE |  |  | PRIMARY KEY |
| 14 | `PHYSICIAN_INITIALS` | VARCHAR(100) |  |  | The initials of the physician. |
| 15 | `PHYSICIAN_LAST_NAME` | VARCHAR(100) |  |  | The last name of the physician. |
| 16 | `PHYSICIAN_MIDDLE_NAME` | VARCHAR(100) |  |  | The middle name of the physician. |
| 17 | `PHYSICIAN_MOBILE` | VARCHAR(100) |  |  | The primary phone number of the physician. |
| 18 | `PHYSICIAN_NAME` | VARCHAR(200) |  |  | The full name of the physician. |
| 19 | `PHYSICIAN_PHONE` | VARCHAR(50) |  |  | The full phone of the physician. |
| 20 | `PHYSICIAN_PREFIX` | VARCHAR(100) |  |  | The prefix of the physician. |
| 21 | `PHYSICIAN_STATE` | VARCHAR(40) |  |  | The state of the physician. |
| 22 | `PHYSICIAN_SUFFIX` | VARCHAR(100) |  |  | The suffix of the physician. |
| 23 | `PHYSICIAN_TITLE` | VARCHAR(100) |  |  | The title of the physician. |
| 24 | `PHYSICIAN_ZIP_CODE` | VARCHAR(25) |  |  | The full code of the physician_zip. |
| 25 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 26 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 27 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

