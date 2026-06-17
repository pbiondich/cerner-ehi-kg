# SN_SUP_CAB_PREF_SEG

> Stores the segment(s) to default supply cabinet information to

**Description:** SN SUPPLY CABINET PREF SEGMENT  
**Table type:** REFERENCE  
**Primary key:** `SN_SUP_CAB_PREF_SEG_ID`  
**Columns:** 9  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AREA_CD` | DOUBLE | NOT NULL |  | The Surgical Area this supply cabinet preference is built for |
| 2 | `DOC_TYPE_CD` | DOUBLE | NOT NULL |  | The document type for which a list of segments and event codes will display |
| 3 | `SEG_CD` | DOUBLE | NOT NULL |  | For this document type, the segment on which supply cabinet data will default |
| 4 | `SN_SUP_CAB_PREF_SEG_ID` | DOUBLE | NOT NULL | PK | The unique identifier for the supply cabinet's segmentPrimary Key |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SN_SUP_CAB_PREF_CLASS](SN_SUP_CAB_PREF_CLASS.md) | `SN_SUP_CAB_PREF_SEG_ID` |
| [SN_SUP_CAB_PREF_FIELD](SN_SUP_CAB_PREF_FIELD.md) | `SN_SUP_CAB_PREF_SEG_ID` |

