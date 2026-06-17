# OMF_ENCNTR_PRSNL_RELTN_ST

> Summary table storing the relationships between encounter records and physicians

**Description:** OMF ENCNTR PRSNL RELTN ST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_NBR` | DOUBLE |  |  | The beginning effective date for the row. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BEG_EFFECTIVE_MIN_NBR` | DOUBLE |  |  | The beginning effective minute for the row |
| 4 | `BEG_EFFECTIVE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 5 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 6 | `ENCNTR_PRSNL_RELTN_ID` | DOUBLE | NOT NULL |  | The unique identifier for the table (from the encntr_prsnl_reltn table). |
| 7 | `ENCNTR_PRSNL_R_CD` | DOUBLE | NOT NULL |  | The code value for the relation between the encounter and the physician. |
| 8 | `END_EFFECTIVE_DT_NBR` | DOUBLE |  |  | The end effective date for the row. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `END_EFFECTIVE_MIN_NBR` | DOUBLE |  |  | The end effective minute for the row. |
| 11 | `END_EFFECTIVE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 12 | `PRIORITY_SEQ` | DOUBLE |  |  | The sequence in which records are written to the table for a given encounter/relation combination. |
| 13 | `PRSNL_PERSON_FT_NAME` | VARCHAR(100) |  |  | The free text name for the physician. |
| 14 | `PRSNL_PERSON_GRP_CD` | DOUBLE | NOT NULL |  | The grouping code for the physician as defined through the OMFGroupingTool. |
| 15 | `PRSNL_PERSON_ID` | DOUBLE | NOT NULL |  | The unique identifier for the person. |
| 16 | `PRSNL_PERSON_KEY` | VARCHAR(125) |  |  | The concatenation of the person_id and free text name for uniqueness within PowerVision. |
| 17 | `PRSNL_PERSON_MED_SPEC_CD` | DOUBLE | NOT NULL |  | The medical specialty code for the physician as defined through the OMFGroupingTool. |
| 18 | `PRSNL_PERSON_POSITION_CD` | DOUBLE | NOT NULL |  | The Cerner-defined position for the prsnl related to the encounter. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

