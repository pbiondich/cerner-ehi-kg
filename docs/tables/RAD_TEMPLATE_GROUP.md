# RAD_TEMPLATE_GROUP

> The Rad_Template_Group table contains general information about a grouping of templates. This can be done by person_id or as a general grouping.

**Description:** Rad Template Group  
**Table type:** REFERENCE  
**Primary key:** `TEMPLATE_GROUP_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASSESSMENT_ID` | DOUBLE |  | FK→ | This identifies the default Assessment that is to be assigned whenever the template is used. |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | The Catalog_Cd is a foreign key to the Order_Catalog table. It uniquely identifies an orderable procedure. |
| 3 | `CLASSIFICATION_CD` | DOUBLE | NOT NULL |  | The Classification_Cd indicates the procedure classification that is associated with the template. |
| 4 | `GROUP_DESC` | VARCHAR(50) |  |  | The Group_Desc describes the template group. |
| 5 | `MOD_TEXT_FLAG` | DOUBLE |  |  | The Mod_Text_Flag indicates if the template requires modifications or not. |
| 6 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 7 | `RECOMMENDATION_ID` | DOUBLE |  | FK→ | This identifies the default recommendation that is to be used whenever the template is used. |
| 8 | `TEMPLATE_GROUP_ID` | DOUBLE | NOT NULL | PK | The Template_Group_Id uniquely identifies a row on the Rad_Template_Group table. It serves no other purpose other than to uniquely identify the row. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ASSESSMENT_ID` | [RAD_FOL_UP_FIELD](RAD_FOL_UP_FIELD.md) | `FOLLOW_UP_FIELD_ID` |
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RECOMMENDATION_ID` | [RAD_FOL_UP_FIELD](RAD_FOL_UP_FIELD.md) | `FOLLOW_UP_FIELD_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RAD_TEMPLATE_ASSOC](RAD_TEMPLATE_ASSOC.md) | `TEMPLATE_GROUP_ID` |

