# ORDER_HEALTH_PLAN_DETAIL

> For every action on an order, this table stores the NCPDP Claim related information per health plan used.

**Description:** Order Health Plan Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQ` | DOUBLE | NOT NULL | FK→ | A sequence number used to identify the order of the actions. |
| 2 | `CARD_HOLDER_IDENT` | VARCHAR(100) | NOT NULL | FK→ | The member number of the subscriber to the health plan. |
| 3 | `DETAIL_FIELD_DT_TM` | DATETIME |  |  | Value of the current detail record if source field contains date/time value. |
| 4 | `DETAIL_FIELD_ID` | DOUBLE | NOT NULL |  | Stores the order entry detail id. Populated only for a Rebill that is valid for all health plans. |
| 5 | `DETAIL_FIELD_IDENT` | DOUBLE | NOT NULL |  | Field ID for the current detail record |
| 6 | `DETAIL_FIELD_MEANING` | VARCHAR(25) | NOT NULL |  | Stores the string meaning of the order_entry_detail. Populated only for a Rebill that is valid for all health plans. |
| 7 | `DETAIL_FIELD_SEQ` | DOUBLE | NOT NULL |  | The sequence for each occurrence of a given Source Field. |
| 8 | `DETAIL_FIELD_TXT` | VARCHAR(250) | NOT NULL |  | The value of the current detail record if source field contains text. |
| 9 | `DETAIL_FIELD_VALUE` | DOUBLE | NOT NULL |  | The value of the current detail record if source field contains numeric or codified value. |
| 10 | `DETAIL_TZ` | DOUBLE | NOT NULL |  | Time zone for the detail_field_dt_tm |
| 11 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | The identifier assigned for a health plan. |
| 12 | `ORDER_HEALTH_PLAN_DTL_ID` | DOUBLE | NOT NULL |  | This field contains the unique value assigned to each order health plan detail row. |
| 13 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique value assigned to each orderable procedure associated with an order. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_SEQ` | [ORDER_HEALTH_PLAN](ORDER_HEALTH_PLAN.md) | `ACTION_SEQUENCE` |
| `CARD_HOLDER_IDENT` | [ORDER_HEALTH_PLAN](ORDER_HEALTH_PLAN.md) | `CARD_HOLDER_IDENT` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `HEALTH_PLAN_ID` | [ORDER_HEALTH_PLAN](ORDER_HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `ORDER_ID` | [ORDER_HEALTH_PLAN](ORDER_HEALTH_PLAN.md) | `ORDER_ID` |

