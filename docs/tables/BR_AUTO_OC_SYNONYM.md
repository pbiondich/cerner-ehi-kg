# BR_AUTO_OC_SYNONYM

> autobuild orderable synonymns

**Description:** BEDROCK AUTO ORDER CATALOG SYNONYM  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_SUBTYPE_CD` | DOUBLE | NOT NULL |  | activity sub type |
| 2 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | activity type |
| 3 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 4 | `CATALOG_CD` | DOUBLE | NOT NULL |  | order catalog id |
| 5 | `CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | order catalog type |
| 6 | `MNEMONIC` | VARCHAR(100) |  |  | legacy short name |
| 7 | `MNEMONIC_KEY_CAP` | VARCHAR(100) |  |  | legacy short name, all caps |
| 8 | `MNEMONIC_TYPE_CD` | DOUBLE | NOT NULL |  | The mnemonic type associated to the order catalog. |
| 9 | `OE_FORMAT_ID` | DOUBLE | NOT NULL |  | Order entry format associated to the synonym. |
| 10 | `SYNONYM_ID` | DOUBLE | NOT NULL |  | Unique identifier for the table |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

