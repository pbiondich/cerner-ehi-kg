# RX_METHOD

> Header table for methods of calculating demographic values. Examples: Body Surface Area, Creatinine Clearance, Adjusted/Ideal body Weight

**Description:** PharmNet Method  
**Table type:** REFERENCE  
**Primary key:** `RX_METHOD_ID`  
**Columns:** 12  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | User-entered data. Example s: the name of the Study that came up with the method, explanation of the calculation. |
| 5 | `METHOD_CD` | DOUBLE | NOT NULL |  | The Code value will contain the method name and description as well as a CDF_MEANING identifying its type i.e. BSA. |
| 6 | `RX_METHOD_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the rx_method table. |
| 7 | `RX_METHOD_P_ID` | DOUBLE | NOT NULL | FK→ | Used for grouping of versions of RX_METHODs. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `RX_METHOD_P_ID` | [RX_METHOD](RX_METHOD.md) | `RX_METHOD_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [RX_FORMULA](RX_FORMULA.md) | `RX_METHOD_ID` |
| [RX_METHOD](RX_METHOD.md) | `RX_METHOD_P_ID` |
| [RX_METHOD_FAC_RELTN](RX_METHOD_FAC_RELTN.md) | `RX_METHOD_ID` |
| [RX_METHOD_RANGE](RX_METHOD_RANGE.md) | `RX_METHOD_ID` |
| [RX_METHOD_RELTN](RX_METHOD_RELTN.md) | `CHILD_METHOD_ID` |
| [RX_METHOD_RELTN](RX_METHOD_RELTN.md) | `PARENT_METHOD_ID` |

