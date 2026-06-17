# DOC_SET_REF

> Defines the container used to store a documentation set.

**Description:** Documentation Set Reference  
**Table type:** REFERENCE  
**Primary key:** `DOC_SET_REF_ID`  
**Columns:** 18  
**Referenced by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ALLOW_COMMENT_IND` | DOUBLE | NOT NULL |  | Determines if comments may be written against the documentation set. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `DOC_SET_DESCRIPTION` | VARCHAR(250) |  |  | A description of a documentation set. |
| 5 | `DOC_SET_NAME` | VARCHAR(40) | NOT NULL |  | The name of a documentation set. |
| 6 | `DOC_SET_NAME_KEY` | VARCHAR(40) | NOT NULL |  | The name value of DOC_SET_NAME in all CAPS with no spaces. |
| 7 | `DOC_SET_REF_ID` | DOUBLE | NOT NULL | PK | Identifies a specific version of a documentation set related to the SET_REF_ID. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `EVENT_CD` | DOUBLE | NOT NULL |  | Type of Doc Set as defined in the event code model. |
| 10 | `EVENT_SET_NAME` | VARCHAR(100) | NOT NULL |  | Name of the Event Set that is associated with the Doc Set. |
| 11 | `LAST_MODIFIED_DT_TM` | DATETIME |  |  | The date and time this doc set was last modified |
| 12 | `PREV_DOC_SET_REF_ID` | DOUBLE | NOT NULL | FK→ | Previous DOC_SET_REF_ID - used for type 2 versioning |
| 13 | `SET_REF_ID` | DOUBLE | NOT NULL |  | Identifies a specific documentation set for all versions of the set hierarchy. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREV_DOC_SET_REF_ID` | [DOC_SET_REF](DOC_SET_REF.md) | `DOC_SET_REF_ID` |

## Referenced by (9)

| From table | Column |
|------------|--------|
| [CNT_DS_KEY](CNT_DS_KEY.md) | `DOC_SET_REF_ID` |
| [DOC_SET_REF](DOC_SET_REF.md) | `PREV_DOC_SET_REF_ID` |
| [DOC_SET_SECTION_REF_R](DOC_SET_SECTION_REF_R.md) | `DOC_SET_REF_ID` |
| [DYNAMIC_LABEL_TEMPLATE](DYNAMIC_LABEL_TEMPLATE.md) | `DOC_SET_REF_ID` |
| [ONC_DOCSETREF_CAT_R](ONC_DOCSETREF_CAT_R.md) | `DOC_SET_REF_ID` |
| [ONC_FORM_ACTIVITY](ONC_FORM_ACTIVITY.md) | `DOC_SET_REF_ID` |
| [ONC_NOMEN_DOCSETREF_R](ONC_NOMEN_DOCSETREF_R.md) | `DOC_SET_REF_ID` |
| [ONC_TOKEN_ELEMENT_R](ONC_TOKEN_ELEMENT_R.md) | `DOC_SET_REF_ID` |
| [ONC_WORKSHEET](ONC_WORKSHEET.md) | `DOC_SET_REF_ID` |

