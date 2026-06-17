# PHA_RX_TRANSFERS

> Table that contains the Retail Transfer Locations

**Description:** PHA RX TRANSFERS  
**Table type:** REFERENCE  
**Primary key:** `RX_TRANSFER_CD`  
**Columns:** 23  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDRESS1` | VARCHAR(100) |  |  | First line of the location address |
| 2 | `ADDRESS2` | VARCHAR(100) |  |  | Second line of the location address |
| 3 | `ADDRESS3` | VARCHAR(100) |  |  | Third line of the location address |
| 4 | `ADDRESS4` | VARCHAR(100) |  |  | Fourth line of the location address |
| 5 | `CITY` | VARCHAR(100) |  |  | Free-text City |
| 6 | `COUNTRY_CD` | DOUBLE | NOT NULL |  | Country |
| 7 | `COUNTY_CD` | DOUBLE | NOT NULL |  | County |
| 8 | `DEA_NBR` | VARCHAR(100) |  |  | DEA Number |
| 9 | `EMAIL` | VARCHAR(100) |  |  | Free-text email address |
| 10 | `FAX` | VARCHAR(100) |  |  | free textfax # |
| 11 | `LICENSE` | VARCHAR(100) |  |  | Free-text License |
| 12 | `PHARMACIST` | VARCHAR(100) |  |  | Name |
| 13 | `PHONE1` | VARCHAR(100) |  |  | Phone number |
| 14 | `PHONE2` | VARCHAR(100) |  |  | Secondary phone |
| 15 | `RX_TRANSFER_CD` | DOUBLE | NOT NULL | PK | Key to this table |
| 16 | `STATE_CD` | DOUBLE | NOT NULL |  | State |
| 17 | `STORE` | VARCHAR(100) |  |  | Free-text Pharmacy Store Number |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 23 | `ZIP_CODE` | VARCHAR(100) |  |  | free textzip code |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RX_SCRIPT_TRANSFER_HX](RX_SCRIPT_TRANSFER_HX.md) | `XFER_RX_TRANSFER_CD` |

