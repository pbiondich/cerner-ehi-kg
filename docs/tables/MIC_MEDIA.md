# MIC_MEDIA

> This table contains the instrument interface translations for each piece of media. Media translations are currently used for blood culture instrument interfaces.

**Description:** Microbiology Inoculation Media  
**Table type:** REFERENCE  
**Primary key:** `MEDIA_CD`  
**Columns:** 9  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `INSTR_TRANS` | CHAR(15) |  |  | This field identifies the description of the media as it exists on the host system(instrument) and identifies how the code will be transmitted to and from the Cerner system. |
| 2 | `MEDIA_CD` | DOUBLE | NOT NULL | PK | This field identifies the code_value of the media for which translations are defined.. Media is defined on code set 2051, Container. |
| 3 | `MEDIA_TYPE_FLAG` | DOUBLE |  |  | This field indicates whether the piece of media is associated with microbiology or virology procedures. |
| 4 | `REQ_ANG_IND` | DOUBLE | NOT NULL |  | This column represents whether media unload required for report generation in ANG. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MIC_MEDIA_ACTIVITY](MIC_MEDIA_ACTIVITY.md) | `MEDIA_CD` |
| [MIC_MEDIA_DEFAULT](MIC_MEDIA_DEFAULT.md) | `MEDIA_CD` |

