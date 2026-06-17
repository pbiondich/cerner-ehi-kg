# PFT_CLAIM_RULE

> Contains Claim generation rules.

**Description:** ProFit Claim Rule  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `MEDIA_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the media type to which the rule applies. |
| 5 | `PFT_CLAIM_RULE_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a claim generation rule. |
| 6 | `PREV_PFT_CLAIM_RULE_ID` | DOUBLE | NOT NULL |  | Used to track versions of the claim rule information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 7 | `RULE_DESC` | VARCHAR(200) |  |  | Textual description of the claim generation rule. |
| 8 | `RULE_NAME` | VARCHAR(100) |  |  | The name of the rule. |
| 9 | `RULE_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies template information for this claim generation rule. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RULE_TEMPLATE_ID` | [LONG_BLOB_REFERENCE](LONG_BLOB_REFERENCE.md) | `LONG_BLOB_ID` |

