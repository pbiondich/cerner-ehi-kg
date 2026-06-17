# BR_CCN_EXTENSION

> Contains attributes of a CCN that require history to be kept.

**Description:** Bedrock CMS Certification Number Extension  
**Table type:** REFERENCE  
**Primary key:** `BR_CCN_EXTENSION_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BR_CCN_EXTENSION_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the BR_CCN_EXTENSION table. |
| 4 | `BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | Identifies the CCN that is the main source for the data on this table. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `MEDICAID_STAGE_CD` | DOUBLE | NOT NULL |  | Stores the stage and year for the Medicaid program enrollment |
| 7 | `MEDICARE_YEAR` | DOUBLE |  |  | The effective year for the Medicare program associated to this CCN |
| 8 | `ORIG_BR_CCN_EXTENSION_ID` | DOUBLE | NOT NULL | FK→ | The PK value of the Original (Effective) Row for this versioned set |
| 9 | `PROGRAM_TYPE_TXT` | VARCHAR(50) | NOT NULL |  | Identifies what type of program this CCN is associated to. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_CCN_ID` | [BR_CCN](BR_CCN.md) | `BR_CCN_ID` |
| `ORIG_BR_CCN_EXTENSION_ID` | [BR_CCN_EXTENSION](BR_CCN_EXTENSION.md) | `BR_CCN_EXTENSION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BR_CCN_EXTENSION](BR_CCN_EXTENSION.md) | `ORIG_BR_CCN_EXTENSION_ID` |

