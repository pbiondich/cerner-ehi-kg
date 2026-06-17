# ORDER_THERAP_SBSTTN

> This table stores the therapeutic substitution information for an order at the ingredient level. When a therapeutic substitution rule is accepted, overridden or an alternate regimen applied to an order, a row will be added to this table.

**Description:** Order Therapeutic Substitution  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQUENCE` | DOUBLE | NOT NULL |  | A sequence number used to identify the order of the actions. |
| 2 | `COMP_SEQUENCE` | DOUBLE | NOT NULL |  | A system assigned number, identifying the order of the ingredient on which the substitution is applied. |
| 3 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | The ID that uniquely identifies the pharmacy product for which the therapeutic substitution rule is applied. This field will reference the item_id field on the medication_definition table. This field must be valued if a therapeutic substitution rule at the product level was accepted. |
| 4 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The ID of the order associated to this substitution. |
| 5 | `ORDER_THERAP_SBSTTN_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the order_therap_sbsttn table. It is a number internally assigned by the system. |
| 6 | `OVERRIDE_REASON_CD` | DOUBLE | NOT NULL |  | Codified value indicating the reason the therapeutic substitution was overridden. When a therapeutic substitution is accepted or an alternate regimen is applied, this field will be 0. If the therapeutic substitution is overridden, this field must contain the reason code value. |
| 7 | `SUBSTITUTION_ACCEPT_FLAG` | DOUBLE | NOT NULL |  | The flag to indicate whether the therapeutic substitution was accepted or overridden. The possible values are 1 = Accept, 2 = Override and 3 = Alternate Regimen. |
| 8 | `THERAP_SBSTTN_ID` | DOUBLE | NOT NULL |  | The ID of the therapeutic substitution rule applied to the order. This field will be 0 if the substitution rule is overridden. If the substitution rule is accepted or an alternate regimen is applied, this field should contain a unique identifier from the rx_therap_sbsttn table. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [MEDICATION_DEFINITION](MEDICATION_DEFINITION.md) | `ITEM_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

