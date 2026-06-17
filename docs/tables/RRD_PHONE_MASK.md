# RRD_PHONE_MASK

> Table containing phone masks which define how a phone number is displayed

**Description:** RRD PHONE MASK  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AREA_CODE` | VARCHAR(25) |  |  | Area Code portion of phone maskColumn |
| 2 | `COUNTRY_CODE` | VARCHAR(25) |  |  | Country code portion of phone maskColumn |
| 3 | `DESCRIPTION` | VARCHAR(50) | NOT NULL |  | Name of phone maskColumn |
| 4 | `EXCHANGE` | VARCHAR(25) |  |  | Exchange portion of phone maskColumn |
| 5 | `PHONE_MASK_ID` | DOUBLE | NOT NULL |  | Unique ID for a phone maskColumn |
| 6 | `SUFFIX` | VARCHAR(50) |  |  | Suffix portion of phone maskColumn |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

