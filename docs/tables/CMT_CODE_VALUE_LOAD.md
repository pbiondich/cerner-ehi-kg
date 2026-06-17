# CMT_CODE_VALUE_LOAD

> Used only to load CMT data to the CODE_VALUE table.

**Description:** CMT_CODE_VALUE_LOAD  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CDF_MEANING` | VARCHAR(12) | NOT NULL |  | Loads CDF_MEANING on CODE_VALUE. |
| 4 | `CKI` | VARCHAR(100) | NOT NULL |  | Loads CKI on CODE_VALUE. |
| 5 | `CODE_SET` | DOUBLE | NOT NULL |  | Loads CODE_SET on CODE_VALUE. |
| 6 | `CODE_VALUE` | DOUBLE | NOT NULL | FK→ | Maps CODE_VALUE from the CODE_VALUE table to a CMT code value |
| 7 | `CODE_VALUE_UUID` | VARCHAR(100) | NOT NULL |  | Loads CODE_VALUE_UUID on CODE_VALUE. |
| 8 | `COLLATION_SEQ` | DOUBLE | NOT NULL |  | Loads COLLATION_SEQ on CODE_VALUE. |
| 9 | `CONCEPT_CKI` | VARCHAR(100) | NOT NULL |  | Loads CONCEPT_CKI on CODE_VALUE. |
| 10 | `DEFINITION` | VARCHAR(100) | NOT NULL |  | Loads DEFINITION on CODE_VALUE. |
| 11 | `DESCRIPTION` | VARCHAR(60) | NOT NULL |  | Loads DESCRIPTION on CODE_VALUE. |
| 12 | `DISPLAY` | VARCHAR(40) | NOT NULL |  | Loads DISPLAY on CODE_VALUE. |
| 13 | `DISPLAY_KEY` | VARCHAR(40) | NOT NULL |  | Loads DISPLAY_KEY on CODE_VALUE. |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `IGNORE_IND` | DOUBLE | NOT NULL |  | Indicates whether to ignore the row inthe Bedrock Wizard |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CODE_VALUE` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

