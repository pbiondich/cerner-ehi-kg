# QMD_PORTAL_PERMISSION

> A table that stores portal configuration settings for the quality measures dashboard.

**Description:** Quality Measures Dashboard Portal Permissions  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLIENT_PORTAL_DISPLAY_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive that would enable client submission portal portal view only on the quality measures dashboard |
| 2 | `DASHBOARD_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive that would enable eligible hospital quality scorecard view only on the quality measures dashboard. |
| 3 | `MIPS_DISPLAY_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive that would enable MIPS portal view only on the quality measures dashboard. |
| 4 | `PRSNL_GROUP_RELTN_ID` | DOUBLE | NOT NULL | FK→ | The ID of the personnel group the permissions are associated to. It is the PK of the PRSNL_GROUP_RELTN table. |
| 5 | `QMD_PORTAL_PERMISSION_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the QMD_PORTAL_PERMISSIONS table. |
| 6 | `QRDA_EXPORT_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. Active means it would enable QRDA export view only on the quality measures dashboard |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_SOURCE` | VARCHAR(40) |  |  | The script name responsible for updating the record. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_GROUP_RELTN_ID` | [PRSNL_GROUP_RELTN](PRSNL_GROUP_RELTN.md) | `PRSNL_GROUP_RELTN_ID` |

