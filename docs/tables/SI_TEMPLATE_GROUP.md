# SI_TEMPLATE_GROUP

> Stores template group relationships along with output content type and default information.

**Description:** System Integration Template Group Relation  
**Table type:** REFERENCE  
**Primary key:** `SI_TEMPLATE_GROUP_ID`  
**Columns:** 14  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CERNER_DEFINED_IND` | DOUBLE |  |  | When set, this template group has been defined by Cerner and templates can't be added or removed from the group. |
| 2 | `DEFAULT_IND` | DOUBLE | NOT NULL |  | This indicates the default template group for a given output_content_type_cd, only one template group per output_content_type_cd can have this set at a time. |
| 3 | `GROUP_DESCRIPTION` | VARCHAR(250) | NOT NULL |  | This field describes the group of templates. |
| 4 | `OUTPUT_CONTENT_TYPE_CD` | DOUBLE | NOT NULL |  | The output type of this set of templates. |
| 5 | `RENDERING_URL` | VARCHAR(256) |  |  | The URL of the rendering style sheet for all documents generated using this Template Group |
| 6 | `SI_TEMPLATE_GROUP_ID` | DOUBLE | NOT NULL | PK | The primary Identifier |
| 7 | `SUMMARY_CARE_TYPE_CD` | DOUBLE | NOT NULL |  | If selected, then this document must meet all required specifications for the selected type. |
| 8 | `SYSTEM_DEFAULT_IND` | DOUBLE | NOT NULL |  | This indicates the default template group for the system, only one template group can have this set at a time. |
| 9 | `TEMPLATE_TYPE_CD` | DOUBLE | NOT NULL |  | When valued, this field will combine with output content type to specify which si_templates can be used. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [SI_DOCUMENT_INFO](SI_DOCUMENT_INFO.md) | `SI_TEMPLATE_GROUP_ID` |
| [SI_ENTITY_TEMPLATE_GROUP_R](SI_ENTITY_TEMPLATE_GROUP_R.md) | `SI_TEMPLATE_GROUP_ID` |
| [SI_TEMPLATE_GROUP_RELTN](SI_TEMPLATE_GROUP_RELTN.md) | `SI_TEMPLATE_GROUP_ID` |

