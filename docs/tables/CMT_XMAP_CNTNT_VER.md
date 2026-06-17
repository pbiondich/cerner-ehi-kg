# CMT_XMAP_CNTNT_VER

> Contains version information for cmt_cross_map content releases

**Description:** CMT crossmap content version  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `CMT_XMAP_CNTNT_VER_ID` | DOUBLE | NOT NULL |  | cmt crossmap content version identifierColumn |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `MAP_FROM_VERSION_FT` | VARCHAR(20) |  |  | Version of source vocablary mean free text field |
| 5 | `MAP_FROM_VERSION_NBR` | DOUBLE | NOT NULL |  | Version of vocabulary mean for the cross-map source |
| 6 | `MAP_FROM_VOCAB_CD` | DOUBLE | NOT NULL |  | Source_vocabulary_cd for the cross-map target |
| 7 | `MAP_TO_VERSION_FT` | VARCHAR(20) |  |  | Version of source vocabulary mean free text field |
| 8 | `MAP_TO_VERSION_NBR` | DOUBLE | NOT NULL |  | map to version numberColumn |
| 9 | `MAP_TO_VOCAB_CD` | DOUBLE | NOT NULL |  | Source_vocabulary_cd for the cross-map target |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

