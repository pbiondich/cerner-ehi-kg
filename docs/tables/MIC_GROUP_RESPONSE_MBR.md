# MIC_GROUP_RESPONSE_MBR

> This table associates the coded responses with the microbiology group response/procedure and service resource.

**Description:** Microbiology Group Response Members  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DETAIL_RESPONSE_CD` | DOUBLE | NOT NULL |  | This field identifies the code_value of the coded response or organism associated with the group response. Fill in the blank coded responses are defined on code set 1022 with a CDF meaning of 'BLANK'. |
| 2 | `GROUP_RESPONSE_ID` | DOUBLE | NOT NULL | FK→ | This field identifies the unique value for group response from the mic_group_response table. |
| 3 | `NEW_PHRASE_IND` | DOUBLE |  |  | This field indicates whether the coded response should display on a new line or display on the current line. Valid values include: 0 = Display on current line 1 = Display on a new line |
| 4 | `RESPONSE_SEQ` | DOUBLE | NOT NULL |  | This field identifies a unique value for each coded response included in the group response. The sequence also determines the order the coded responses were entered into the group response. |
| 5 | `STATISTICS_IND` | DOUBLE |  |  | Determines whether or not a group or details within a group are sent to the archive model for statistical purposes |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `GROUP_RESPONSE_ID` | [MIC_GROUP_RESPONSE](MIC_GROUP_RESPONSE.md) | `GROUP_RESPONSE_ID` |

