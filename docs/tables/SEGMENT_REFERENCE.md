# SEGMENT_REFERENCE

> Contains the attributes associated with a documentation segment

**Description:** Segment Reference  
**Table type:** REFERENCE  
**Primary key:** `SEG_CD`  
**Columns:** 33  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context responsible for inserting this row on the table |
| 6 | `CREATE_DT_TM` | DATETIME |  |  | The date and time this row was inserted on the table |
| 7 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The person responsible for inserting this row on the table |
| 8 | `CREATE_TASK` | DOUBLE |  |  | The task responsible for inserting this row on the table |
| 9 | `DOC_TYPE_CD` | DOUBLE | NOT NULL |  | The document type associated with this documentation segment, i.e. OR Nursing Record, Preop Nursing Assessment |
| 10 | `EQUIP_CLASS_NODE_ID` | DOUBLE | NOT NULL | FK→ | *** OBSOLETE ***Column |
| 11 | `EXECUTE_SEQ` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 12 | `INPUT_FORM_CD` | DOUBLE | NOT NULL |  | The input form associated with this documentation segment. This is the form that will be launched by the form builder when this segment is selected in the Segment Navigator |
| 13 | `OBJECT_NAME` | VARCHAR(50) |  |  | *** OBSOLETE ***Column |
| 14 | `POST_CARE_TEXT_ID` | DOUBLE | NOT NULL | FK→ | A reference (foreign key) to the long_text table identifying the care text that should print AFTER this segment on the intraoperative record. |
| 15 | `PREF_CARD_DEFAULTS_IND` | DOUBLE |  |  | An indicator of whether or not preference card defaults may exist for this documentation segment |
| 16 | `PRE_CARE_TEXT_ID` | DOUBLE | NOT NULL | FK→ | A reference (foreign key) to the long_text table identifying the care text that should print BEFORE this segment on the intraoperative record. |
| 17 | `PRINTABLE_IND` | DOUBLE |  |  | An indicator of whether or not this segment is printable on the Intraoperative Record or not. Unchartable Events is an example of a segment that may have a printable indicator of 0. The default is 1. |
| 18 | `PRINT_SEQ` | DOUBLE |  |  | This defines the printing sequence for the segment in the Preference Card defaults and the Perioperative Record |
| 19 | `REQUIRED_FIELD_IND` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 20 | `SEG_CD` | DOUBLE | NOT NULL | PK FK→ | The primary key, uniquely identifying a row on this table. |
| 21 | `SEG_GRP_CD` | DOUBLE | NOT NULL | FK→ | The segment group of which this segment is a part of. Each segment may only be contained in one segment group. |
| 22 | `SEG_REQ_FLAG` | DOUBLE |  |  | Indicates whether this segment is required within the document type. If the value is 1 (system required) or 2 (site required), the Perioperative Document Manager will not allow a "Delete" or "N/A" of this segment. |
| 23 | `SEG_SEQ` | DOUBLE |  |  | The absolute sequence of this segment within the specified document type. |
| 24 | `SIGNATURE_FLAG` | DOUBLE | NOT NULL |  | Indicates if the segment allows or requires electronic signature (0 = does not allow or require signature, 1 = allows signature, 2 = requires signature) |
| 25 | `SURG_AREA_CD` | DOUBLE | NOT NULL |  | The surgical area associated with this documentation segment. Identified by a CDF Meaning of "SURGAREA" on the Service Resource codeset. |
| 26 | `SYSTEM_DEFINED_IND` | DOUBLE |  |  | An indicator of whether or not this segment is system-defined. |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 32 | `VERBAL_ORDERS_IND` | DOUBLE | NOT NULL |  | This marks the segment as being part of the Verbal Orders Review Process. |
| 33 | `VERIFY_SCRIPT_NAME` | VARCHAR(50) |  |  | *** OBSOLETE ***Column |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EQUIP_CLASS_NODE_ID` | [CLASS_NODE](CLASS_NODE.md) | `CLASS_NODE_ID` |
| `POST_CARE_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PRE_CARE_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `SEG_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SEG_GRP_CD` | [SEGMENT_GRP_REFERENCE](SEGMENT_GRP_REFERENCE.md) | `SEG_GRP_CD` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SEG_GRP_SEQ_R](SEG_GRP_SEQ_R.md) | `SEG_CD` |

