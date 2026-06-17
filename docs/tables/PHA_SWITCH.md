# PHA_SWITCH

> contains Switch information

**Description:** Contains Switch information for adjudication  
**Table type:** REFERENCE  
**Primary key:** `SWITCH_CD`  
**Columns:** 22  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTACT` | VARCHAR(100) |  |  | Contact name |
| 2 | `DIAL_CMD` | VARCHAR(100) |  |  | Dial command |
| 3 | `EMAIL` | VARCHAR(100) |  |  | Email |
| 4 | `ESCAPE_CMD` | VARCHAR(100) |  |  | Escape command |
| 5 | `FAX` | VARCHAR(100) |  |  | Fax number |
| 6 | `INITIALIZE_CMD` | VARCHAR(100) |  |  | Initialize command |
| 7 | `MODEM_PHONE1` | VARCHAR(100) |  |  | Modem Phone 1 |
| 8 | `MODEM_PHONE2` | VARCHAR(100) |  |  | Modem Phone 2 |
| 9 | `MODEM_PHONE3` | VARCHAR(100) |  |  | Modem phone 3 |
| 10 | `MODEM_PHONE4` | VARCHAR(100) |  |  | Modem phone 4 |
| 11 | `NOTES` | VARCHAR(255) |  |  | notes |
| 12 | `PHONE1` | VARCHAR(100) |  |  | Phone |
| 13 | `PHONE2` | VARCHAR(100) |  |  | Phone 2 |
| 14 | `PORT` | VARCHAR(100) |  |  | Port |
| 15 | `PROTOCOL_CD` | DOUBLE | NOT NULL |  | Protocol Code |
| 16 | `SWITCH_CD` | DOUBLE | NOT NULL | PK | Switch Code |
| 17 | `SYSTEM_NUMBER` | VARCHAR(100) |  |  | System number |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PHA_SWITCH_CONN_R](PHA_SWITCH_CONN_R.md) | `SWITCH_CD` |

