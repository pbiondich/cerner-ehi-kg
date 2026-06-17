# RX_CLAIM_OVERRIDE

> Stores the values of fields, which are part of claim request message, overridden by the user.

**Description:** RX Claim Override  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CARD_HOLDER_IDENT` | VARCHAR(100) | NOT NULL |  | The member number of the subscriber to the health plan. |
| 2 | `DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | Relates a particular field to a specific row on the Dispense History table. |
| 3 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | This column relates a particular field to a specific health plan record. |
| 4 | `OVERRIDE_FIELD_CD` | DOUBLE | NOT NULL |  | National Council for Prescription Drug Program Code taken from code_value , code_set 4517. |
| 5 | `OVERRIDE_FIELD_SEQ` | DOUBLE | NOT NULL |  | Sequence that indicates the multiple occurrences of a particular field_cd. |
| 6 | `OVERRIDE_FIELD_TXT` | VARCHAR(255) | NOT NULL |  | Value entered by the user for a given field_cd and field_seq combination. |
| 7 | `RX_CLAIM_OVERRIDE_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a specific override field. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |

