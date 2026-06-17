# MLTM_SYST_IDENTIFIER

> This table defines a body system (i.e., hematologic, hepatic, respiratory, etc.).

**Description:** Multum SYST Identifier  
**Table type:** REFERENCE  
**Primary key:** `SYST_ID`  
**Columns:** 7  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `SYST_ID` | DOUBLE | NOT NULL | PK | This field contains a numeric identifier for a side effect system. |
| 2 | `SYST_NAME` | VARCHAR(30) |  |  | This field contains a textual description of a body system represented by syst_id. For example, syst_id 1 has a syst_name of hematologic. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MLTM_XP_CLIN_TEXT_XREF](MLTM_XP_CLIN_TEXT_XREF.md) | `SYST_ID` |

