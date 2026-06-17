# RAD_TEMPLATE_ASSOC

> The Rad_Templete_Assoc table contains a list of templates

**Description:** Rad Template Association  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | The Task_Assay_Cd is a foreign key to the Discrete_Task_Assay table. It identifies which report detail that the template is associated with. |
| 2 | `TEMPLATE_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The Template_Group_Id is a foreign key to the Rad_Template_Group table. |
| 3 | `TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | The Template_Id is a foreign key to the WP_Template table. It uniquely identify a template. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |
| `TEMPLATE_GROUP_ID` | [RAD_TEMPLATE_GROUP](RAD_TEMPLATE_GROUP.md) | `TEMPLATE_GROUP_ID` |
| `TEMPLATE_ID` | [WP_TEMPLATE](WP_TEMPLATE.md) | `TEMPLATE_ID` |

