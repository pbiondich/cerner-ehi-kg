# CREDIT_CARD_RELTN

> Relates credit card information to person and/or formal payment plan rows.

**Description:** Credit Card Relationship  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `CREDIT_CARD_RELTN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a relationship between credit card information, a person, and/or a formal payment plan. |
| 5 | `CREDIT_CARD_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of credit card. |
| 6 | `DISPLAY_TXT` | VARCHAR(250) |  |  | The dispalyable masked credit card number. |
| 7 | `EXPIRATION_DT_TM` | DATETIME |  |  | The date and time the credit card will expire. |
| 8 | `MERCHANT_IDENT` | VARCHAR(250) |  |  | Identifier for the credit card vendor. |
| 9 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely associates the credit card to one or more persons (card on file). |
| 10 | `PFT_PAYMENT_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Associates the credit card to one or more payment plans. |
| 11 | `TOKEN_TXT` | VARCHAR(250) |  |  | A reference value used for charging a credit card. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PFT_PAYMENT_PLAN_ID` | [PFT_PAYMENT_PLAN](PFT_PAYMENT_PLAN.md) | `PFT_PAYMENT_PLAN_ID` |

