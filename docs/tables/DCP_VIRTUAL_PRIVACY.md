# DCP_VIRTUAL_PRIVACY

> Specifies the patient's privacy for an INet Virtual Call

**Description:** Patient Privacy for INet Virtual Call  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUDIO_OVERRIDE_IND` | DOUBLE |  |  | Specifies whether the privacy is eligible for audio override |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `DCP_VIRTUAL_PRIVACY_ID` | DOUBLE | NOT NULL |  | Primary KeyColumn |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `FREETEXT_COMMENT` | VARCHAR(255) |  |  | Specifies the Free Text Comment |
| 6 | `PERSON_ID` | DOUBLE | NOT NULL |  | Specifies the Person the privacy is set for |
| 7 | `PRIVACY_CD` | DOUBLE | NOT NULL |  | Specifies the type of privacy set |
| 8 | `PRIVACY_COMMENT_CD` | DOUBLE | NOT NULL |  | Specifies the comment type |
| 9 | `TEMPORARY_IND` | DOUBLE |  |  | Specifies whether the privacy is permanent (no expiration) or temporary. 0 = Permanent, 1 = Temporary |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `VIDEO_OVERRIDE_IND` | DOUBLE |  |  | Specifies whether the privacy is eligible for video override |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

