# ONC_DOCSET_ELEM_DECORATOR

> Defines display attributes of a doc set element

**Description:** Doc Set Element Decorator  
**Table type:** REFERENCE  
**Primary key:** `ONC_DOCSET_ELEM_DECORATOR_ID`  
**Columns:** 17  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `DOC_SET_ELEMENT_ID` | DOUBLE | NOT NULL | FK→ | The id of the doc set element that is decorated. |
| 4 | `ELEMENT_STYLE_FLAG` | DOUBLE | NOT NULL |  | An enumeration specifying what element style to apply when displaying the element: 0: Default 1: Use Radio Buttons for Alpha Responses. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `END_GROUP_TYPE_FLAG` | DOUBLE | NOT NULL |  | BitMask of enumerations for the type of group that is being ended: 0 (10) = 0 + 0 + 0 -> none 1 (10) = 0 + 0 + 1 -> tab 2 (10) = 0 + 10 + 0 -> frame 3 (10) = 0 + 10 + 1 -> tab and frame 4 (10) = 100 + 0 + 0 -> horizontal list 5 (10) = 100 + 0 + 1 -> horizontal list and tab. 6 (10) = 100 + 10 + 0 -> horizontal list and frame 7 (10) = 100 + 10 + 1 -> horizontal list and frame and tab. |
| 7 | `GROUP_CAPTION` | VARCHAR(256) | NOT NULL |  | The caption to use for the element group that is being started. When multiple group types are started simultaneously, '%~' will be interpreted as a delimiter so separate captions can be specified for each. The fields in the delimited string will be applied in increasing order by group type enumeration value. |
| 8 | `GROUP_END_IND` | DOUBLE | NOT NULL |  | Specifies to stop the last started element groups matching the group_type_flag |
| 9 | `GROUP_START_IND` | DOUBLE | NOT NULL |  | Specifies to start one element group for each group type represented in the group_type_flag. When multiple groups are provided they will be started in increasing order by group type enumeration value |
| 10 | `ONC_DOCSET_ELEM_DECORATOR_ID` | DOUBLE | NOT NULL | PK | Primary key |
| 11 | `PREV_DOCSET_ELEM_DECORATOR_ID` | DOUBLE | NOT NULL | FK→ | Previous Doc Set Section Element Decorator Id Used for Type 2 versioning |
| 12 | `START_GROUP_TYPE_FLAG` | DOUBLE | NOT NULL |  | BitMask of enumerations for the type of group that is being started: 0 (10) = 0 + 0 + 0 -> none 1 (10) = 0 + 0 + 1 -> tab 2 (10) = 0 + 10 + 0 -> frame 3 (10) = 0 + 10 + 1 -> tab and frame 4 (10) = 100 + 0 + 0 -> horizontal list 5 (10) = 100 + 0 + 1 -> horizontal list and tab. 6 (10) = 100 + 10 + 0 -> horizontal list and frame 7 (10) = 100 + 10 + 1 -> horizontal list and frame and tab. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DOC_SET_ELEMENT_ID` | [DOC_SET_ELEMENT_REF](DOC_SET_ELEMENT_REF.md) | `DOC_SET_ELEMENT_ID` |
| `PREV_DOCSET_ELEM_DECORATOR_ID` | [ONC_DOCSET_ELEM_DECORATOR](ONC_DOCSET_ELEM_DECORATOR.md) | `ONC_DOCSET_ELEM_DECORATOR_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ONC_DOCSET_ELEM_DECORATOR](ONC_DOCSET_ELEM_DECORATOR.md) | `PREV_DOCSET_ELEM_DECORATOR_ID` |

