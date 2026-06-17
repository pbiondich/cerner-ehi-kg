# LH_VIEWS

> This table is used to gather patient's view dates to be used for Meaningful Use Functional Reporting's VDT measure

**Description:** LH VIEWS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `D_PERSON_ID` | DOUBLE | NOT NULL |  | Identifies the person associated with the quality measure. Foreign key to the LH_D_PERSON table |
| 2 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time that the record was extracted from the source system |
| 3 | `LH_VIEWS_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 5 | `PERSON_ID` | DOUBLE | NOT NULL |  | Indicates the person_id of the patient with a view |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The source that updated the row of data |
| 9 | `VDT_VIEW_DT_TM` | DATETIME |  |  | The date/time the patient viewed data |
| 10 | `VDT_VIEW_LOC_DT_TM` | DATETIME |  |  | The date/time the patient viewed data; Normalized to GMT |
| 11 | `VDT_VIEW_TYPE` | VARCHAR(50) |  |  | Indicates the type of view by the patient |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

