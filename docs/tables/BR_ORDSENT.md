# BR_ORDSENT

> Stores order sentences and their display lines

**Description:** Bedrock Order Sentence  
**Table type:** REFERENCE  
**Primary key:** `BR_ORDSENT_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_ORDSENT_ID` | DOUBLE | NOT NULL | PK | Unique ID for the table |
| 2 | `CATALOG_CKI` | VARCHAR(255) | NOT NULL |  | CKI for the associated orderable |
| 3 | `MMDC` | VARCHAR(255) | NOT NULL |  | main Multum drug code |
| 4 | `ORDSENT_COUNT` | DOUBLE | NOT NULL |  | number of times sentences appeared in activity data |
| 5 | `ORDSENT_DISPLAY` | VARCHAR(255) |  |  | Order Sentence display column |
| 6 | `SOURCE_FLAG` | DOUBLE |  |  | where sentence was retrieved from, 1: activity data |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BR_ORDSENT_DETAIL](BR_ORDSENT_DETAIL.md) | `BR_ORDSENT_ID` |

