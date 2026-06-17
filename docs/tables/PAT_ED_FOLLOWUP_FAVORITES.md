# PAT_ED_FOLLOWUP_FAVORITES

> This will store the patient education followup favorites for clinicians to have easier access to.

**Description:** pat_ed_followup_favorites  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMMENT_TXT_ID` | DOUBLE | NOT NULL | FK→ | Comment text added to the follow-up- FK from LONG_TEXT table |
| 2 | `PAT_ED_FOLLOWUP_FAVORITES_ID` | DOUBLE | NOT NULL |  | %followup% |
| 3 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Provider Identifier |
| 4 | `RECIPIENT_TXT_ID` | DOUBLE | NOT NULL | FK→ | External recipient email added to the follow-up- FK from long text table |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `WHEN_DT_TM` | DATETIME |  |  | %followup% |
| 11 | `WHEN_IN_TYPE_FLAG` | DOUBLE |  |  | Value to identify in selection |
| 12 | `WHEN_IN_VAL` | DOUBLE |  |  | Integer of the In value associated with when_in_type_flag |
| 13 | `WHEN_NEEDED_IND` | DOUBLE |  |  | %followup% |
| 14 | `WHEN_WITHIN_CD` | DOUBLE | NOT NULL |  | WHEN WITHIN SELECTION CODE FROM CODESET 27980 |
| 15 | `WHERE_TXT_ID` | DOUBLE | NOT NULL | FK→ | Where text added to the follow-up FK from LONG_TEXT table |
| 16 | `WHO_ID` | DOUBLE | NOT NULL |  | Id value of the who context |
| 17 | `WHO_NAME` | VARCHAR(30) |  |  | NAME OF THE TABLE PROVIDING VALUE FOR THE WHO_ID Field |
| 18 | `WHO_STRING` | VARCHAR(255) |  |  | String value of the who context |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_TXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RECIPIENT_TXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `WHERE_TXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

