# AP_PREFIX_ACCN_TEMPLATE_R

> This reference tables contains valid 'accessioning_templates' for a given prefix.

**Description:** AP Prefix Accessioning Tempate Resolution table  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEFAULT_IND` | DOUBLE |  |  | This field is used to define the 'default' accessioning template for a prefix. |
| 2 | `PREFIX_ID` | DOUBLE | NOT NULL | FK→ | This field contains the reference to the prefix to which the accessioning template is associated. This field contains the foreign key value used to join to the prefix information stored on the AP_PREFIX table. |
| 3 | `TEMPLATE_CD` | DOUBLE | NOT NULL |  | This field contains the foreign key value (representing the accessioning template associated with the prefix) used to join to the accessioning template information stored on code_set 16689. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREFIX_ID` | [AP_PREFIX](AP_PREFIX.md) | `PREFIX_ID` |

