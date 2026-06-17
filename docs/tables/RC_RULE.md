# RC_RULE

> Store business rules for revenue cycle.

**Description:** Revenue Cycle Rule  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time this row was created. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a row on the table specified by the corresponding PARENT_ENTITY_NAME column. Identifies the table for which this rule was created. |
| 6 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Identifies the Parent Entity Table for which this rule was created. |
| 7 | `RAW_RULE_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the row on the long_text_reference table where the raw data of the rule is stored. |
| 8 | `RC_RULE_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a given rule. |
| 9 | `TRSNL_RULE_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Stores the translated business rule(machine readable rule). |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RAW_RULE_LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `TRSNL_RULE_LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

