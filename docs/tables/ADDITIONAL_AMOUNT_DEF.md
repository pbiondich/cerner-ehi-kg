# ADDITIONAL_AMOUNT_DEF

> Additional amounts associated with an item or location or item/location.

**Description:** ADDITIONAL AMOUNT DEF  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDITIONAL_AMOUNT_CD` | DOUBLE | NOT NULL |  | Additional amount Code |
| 2 | `ADDITIONAL_AMOUNT_DEF_ID` | DOUBLE | NOT NULL |  | Primary key |
| 3 | `COST_CENTER_CD` | DOUBLE | NOT NULL |  | Cost center |
| 4 | `INCLUDE_EXCLUDE_IND` | DOUBLE | NOT NULL |  | Apply / don't apply? Yes/No |
| 5 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to an item. |
| 6 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Location code value |
| 7 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 8 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to the Organization table. |
| 9 | `SUB_ACCOUNT_CD` | DOUBLE | NOT NULL |  | Sub account code |
| 10 | `TAX_OVERRIDE_IND` | DOUBLE | NOT NULL |  | This indicator will determine whether the tax set at an item level will override the tax set at organization level. |
| 11 | `TAX_TYPE_CD` | DOUBLE | NOT NULL |  | Tax Type Code from code set 14066 |
| 12 | `TAX_VALUE` | DOUBLE | NOT NULL |  | Tax Value amount |
| 13 | `TAX_VALUE_FLAG` | DOUBLE | NOT NULL |  | This flag indicates whether tax value is a percentage or fixed amount. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_MASTER](ITEM_MASTER.md) | `ITEM_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

