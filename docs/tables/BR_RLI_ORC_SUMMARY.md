# BR_RLI_ORC_SUMMARY

> Reference Lab order change log

**Description:** BEDROCK RLI ORC SUMMARY  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCN_CLASS` | VARCHAR(100) |  |  | The alias value for an accession class, used for modification tracking |
| 2 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 3 | `COLL_CLASS` | VARCHAR(100) |  |  | The alias value for a collection class, used for modification tracking |
| 4 | `COLL_METHOD` | VARCHAR(100) |  |  | The alias value for a collection method, used for modification tracking |
| 5 | `CONTAINER1` | VARCHAR(100) |  |  | The alias value for a specimen container, used for modification tracking |
| 6 | `CONTAINER2` | VARCHAR(100) |  |  | The alias value for a specimen container, used for modification tracking |
| 7 | `CONTAINER3` | VARCHAR(100) |  |  | The alias value for a specimen container, used for modification tracking |
| 8 | `CONTAINER4` | VARCHAR(100) |  |  | The alias value for a specimen container, used for modification tracking |
| 9 | `CONTAINER5` | VARCHAR(100) |  |  | The alias value for a specimen container, used for modification tracking |
| 10 | `MIN_VOL` | VARCHAR(100) |  |  | The alias value for a minimum volume, used for modification tracking |
| 11 | `RLI_ORDER_ID` | DOUBLE | NOT NULL |  | Unique identifier for an RLI order catalog item |
| 12 | `SEQUENCE` | DOUBLE | NOT NULL |  | Sequence |
| 13 | `SPECIAL_HANDLING` | VARCHAR(100) |  |  | The alias value for a special handling code, used for modification tracking |
| 14 | `SPEC_TYPE` | VARCHAR(100) |  |  | The alias value for a specimen type, used for modification tracking |
| 15 | `SUPPLIER_FLAG` | DOUBLE | NOT NULL |  | Unique identifier for an RLI supplier |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

