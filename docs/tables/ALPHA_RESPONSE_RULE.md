# ALPHA_RESPONSE_RULE

> Contains rules related to a given alpha response.

**Description:** Alpha Response Rule  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALPHA_RESPONSE_RULE_ID` | DOUBLE | NOT NULL |  | Uniquely identifies an alpha response rule. |
| 6 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Used in combination with the Reference_Range_Factor_ID to determine the unique alpha response related to this alpha response rule. |
| 7 | `REFERENCE_RANGE_FACTOR_ID` | DOUBLE | NOT NULL | FK→ | Used in combination with the Nomenclature_ID to determine the unique alpha response related to this alpha response rule. |
| 8 | `REF_RANGE_FACTOR_RULE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the reference range factor rule related to the alpha response rule. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOMENCLATURE_ID` | [ALPHA_RESPONSES](ALPHA_RESPONSES.md) | `NOMENCLATURE_ID` |
| `REFERENCE_RANGE_FACTOR_ID` | [ALPHA_RESPONSES](ALPHA_RESPONSES.md) | `REFERENCE_RANGE_FACTOR_ID` |
| `REF_RANGE_FACTOR_RULE_ID` | [REF_RANGE_FACTOR_RULE](REF_RANGE_FACTOR_RULE.md) | `REF_RANGE_FACTOR_RULE_ID` |

