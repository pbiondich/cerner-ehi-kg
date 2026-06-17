# BB_SPEC_EXP_OVRD_PROD

> This table records the crossmatches affected when the user overrides (shortens or extends) the default specimen expiration date and time or when the system overrides the specimen expiration using a flex parameter.

**Description:** Blood Bank Specimen Expire Override Product  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BB_SPEC_EXPIRE_OVRD_ID` | DOUBLE | NOT NULL | FK→ | Uniquely relates this product to the bb_spec_expire_ovrd table. |
| 2 | `BB_SPEC_EXP_OVRD_PROD_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the crossmatch affected when the user overrides the default specimen or when the system overrides the specimen expiration using a flex parameter. |
| 3 | `NEW_XM_EXPIRE_DT_TM` | DATETIME |  |  | Date and time a specimen were collected for a person. |
| 4 | `PREV_XM_EXPIRE_DT_TM` | DATETIME |  |  | New Specimen expire date as it existed before the override. This may have been based on the default or flex expiration or the date from a previous override. |
| 5 | `PRODUCT_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Contains the identifier relating this specimen override to a unique product event. |
| 6 | `PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the product related to this specimen override. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BB_SPEC_EXPIRE_OVRD_ID` | [BB_SPEC_EXPIRE_OVRD](BB_SPEC_EXPIRE_OVRD.md) | `BB_SPEC_EXPIRE_OVRD_ID` |
| `PRODUCT_EVENT_ID` | [PRODUCT_EVENT](PRODUCT_EVENT.md) | `PRODUCT_EVENT_ID` |
| `PRODUCT_ID` | [PRODUCT](PRODUCT.md) | `PRODUCT_ID` |

