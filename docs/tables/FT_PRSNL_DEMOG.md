# FT_PRSNL_DEMOG

> Contains free text demographic information about providers (i.e. name, address from 3rd party services).

**Description:** Free Text Personnel Demographic  
**Table type:** ACTIVITY  
**Primary key:** `FT_PRSNL_DEMOG_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CITY_NAME` | VARCHAR(255) |  |  | The name of the city of the personnel. |
| 2 | `FIRST_NAME` | VARCHAR(255) |  |  | The first name of the personnel. |
| 3 | `FT_PRSNL_DEMOG_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the FT_PRSNL_DEMOG table. |
| 4 | `LAST_NAME` | VARCHAR(255) |  |  | The last name of the personnel. |
| 5 | `MIDDLE_NAME` | VARCHAR(255) |  |  | The middle name of the personnel. |
| 6 | `PREFIX_NAME` | VARCHAR(255) |  |  | The prefix name of the personnel. |
| 7 | `STATE_NAME` | VARCHAR(255) |  |  | The state name of the personnel. |
| 8 | `STREET2_ADDR` | VARCHAR(255) |  |  | The 2nd line of the address of the personnel. |
| 9 | `STREET_ADDR` | VARCHAR(255) |  |  | The street address of the personnel. |
| 10 | `SUFFIX_NAME` | VARCHAR(255) |  |  | The suffix name of the personnel. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 16 | `ZIP_CODE` | VARCHAR(255) |  |  | The zip code of the personnel. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [FT_PRSNL_CONTACT](FT_PRSNL_CONTACT.md) | `FT_PRSNL_DEMOG_ID` |

