# BB_ALPHA_TRANSLATION

> This table only applies to blood products, not derivatives. It allows the system to translate the barcoded version of the unit number into the eye-readable version. Mostly applies to products from American Red Cross.

**Description:** Blood Bank Alpha Translation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALPHA_BARCODE_VALUE` | CHAR(5) | NOT NULL |  | The value of the barcode which should be translated into a different character. Usually it is 2 digits that are translated into a letter for Red Cross units. |
| 6 | `ALPHA_TRANSLATION_ID` | DOUBLE | NOT NULL |  | An internal system-assigned number that ensures the uniqueness of each row. |
| 7 | `ALPHA_TRANSLATION_VALUE` | CHAR(5) |  |  | Only applies to blood products. Defines the letter(s) into which the first two digits of the product number should be translated, e.g., "G" for 12. This way the product number can be barcoded in as "1212345" and translated into "G12345" which is the eye-readable number on the bag. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

