# SI_ENTITY_TEMPLATE_GROUP_R

> Stores template group information related to external entities such as Device_Output_Reltn.

**Description:** System Integration Device Output Template Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEFAULT_IND` | DOUBLE | NOT NULL |  | When this field is set to 1,the relationship is considered the default template group for the given entity. |
| 2 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The ID of the table that relates information to template groups. Initially it will be DEVICE_OUTPUT_RELTN |
| 3 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The name of the table that relates information to template groups. |
| 4 | `REPORT_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | foreign key value from the cr_report_template table. |
| 5 | `RESULT_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates the type of report being generated. This is used as part of the decision porcess for finding Template Groups |
| 6 | `SI_ENTITY_TEMPLATE_GROUP_R_ID` | DOUBLE | NOT NULL |  | The primary Identifier |
| 7 | `SI_TEMPLATE_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the SI_TEMPLATE_GROUP table. This will tie the selected template group with the appropriate device/output combination. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REPORT_TEMPLATE_ID` | [CR_REPORT_TEMPLATE](CR_REPORT_TEMPLATE.md) | `REPORT_TEMPLATE_ID` |
| `SI_TEMPLATE_GROUP_ID` | [SI_TEMPLATE_GROUP](SI_TEMPLATE_GROUP.md) | `SI_TEMPLATE_GROUP_ID` |

