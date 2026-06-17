# SI_COMSRV_MSG_MAP_R

> This table stores the relationships between the SI_MESSAGE and SI_MAPPING_OBJECT

**Description:** This table stores the relationships between UI messages and the mapping objects.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was created.Column |
| 3 | `MAP_ID` | DOUBLE | NOT NULL | FK→ | This is foreign key into the SI_MAPPING_OBJECT table. It identifies a mapping object required of processing of UI message. |
| 4 | `MESSAGE_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key into the SI_MESSAGE table. It indicates for which UI message the row applies. |
| 5 | `PARAM_GROUP_ID` | DOUBLE | NOT NULL |  | This is a foreign key into the SI_PARAMETER table. It indicates the group of parameters that apply to this mapping object for the given UI message. |
| 6 | `SEQ_NUM` | DOUBLE | NOT NULL |  | Indicates the order in which the mapping objects should be executed for the given UI message. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MAP_ID` | [SI_MAPPING_OBJECT](SI_MAPPING_OBJECT.md) | `MAP_ID` |
| `MESSAGE_ID` | [SI_MESSAGE](SI_MESSAGE.md) | `MESSAGE_ID` |

